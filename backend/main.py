import base64
import os
from io import BytesIO
import numpy as np
from numpy import ndarray
from PIL import Image
from imgbeddings import imgbeddings
import faiss
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from fastapi.responses import HTMLResponse
templates = Jinja2Templates(directory="templates")

app = FastAPI()

index = None
all_images = None
ibed = None
index_built = False

def get_subfolder_paths(root_folder):
    subfolder_paths = []
    for foldername, subfolders, filenames in os.walk(root_folder):
        for subfolder in subfolders:
            subfolder_path = os.path.join(foldername, subfolder)
            subfolder_paths.append(subfolder_path)
    return subfolder_paths

def load_images_from_folder(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(folder_path, filename)
            image = Image.open(img_path)
            images.append((filename, image))
    return images

def compute_embeddings(image_list, ibed):
    embeddings = []
    for filename, image in image_list:
        add_embedding = ibed.to_embeddings(image)
        flattened_embedding = np.array(add_embedding).flatten()
        embeddings.append(flattened_embedding)
    return np.array(embeddings)

def similarity_search(query_embedding, index, k=5):
    distances, indices = index.search(query_embedding, k)
    return distances, indices

def build_faiss_index():
    global index, all_images, ibed, index_built
    root_folder_path = './static/images'
    subfolder_paths_list = get_subfolder_paths(root_folder_path)
    sub_folder_path_list1 = [path.replace('\\', '/') for path in subfolder_paths_list]

    all_images = []
    for folder in sub_folder_path_list1:
        images = load_images_from_folder(folder)
        all_images.extend(images)

    ibed = imgbeddings()  # Assuming imgbeddings is imported correctly
    sample_embedding = ibed.to_embeddings(all_images[0][1])
    d = len(np.array(sample_embedding).flatten())
    index = faiss.IndexFlatL2(d)

    embeddings = compute_embeddings(all_images, ibed)
    index.add(embeddings)
    index_built = True

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow requests from the React frontend
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload(request: Request,file: UploadFile = File(...)):
    global index_built, index, all_images, ibed

    if not index_built:
        build_faiss_index()

    contents = await file.read()
    image = Image.open(BytesIO(contents))
    query_embedding = ibed.to_embeddings(image)

    distances, indices = similarity_search(query_embedding, index)
    highest_similarity_index = indices[0][0]
    highest_similarity_image = all_images[highest_similarity_index][1]  # Get the image from the tuple
    highest_similarity_score = 1 / (1 + distances[0][0])

    with BytesIO() as output_bytes:
        image.save(output_bytes, format='JPEG')
        image_data = output_bytes.getvalue()

    query_image_base64 = base64.b64encode(image_data).decode('utf-8')

    with BytesIO() as output_bytes:
        highest_similarity_image.save(output_bytes, format='JPEG')
        similarity_image_data = output_bytes.getvalue()

    matched_image_base64 = base64.b64encode(similarity_image_data).decode('utf-8')

    # Construct inline HTML with both images
    # html_content = f"""
    #     <div style="display: flex; justify-content: flex-end;">
    #         <div style="text-align: right; margin-right: 20px;">
    #             <h2>Query Image:</h2>
    #             <img src="data:image/jpeg;base64,{query_image_base64}" alt="Query Image" style="max-width: 300px;"/>
    #             <h2>Matched Image:</h2>
    #             <img src="data:image/jpeg;base64,{matched_image_base64}" alt="Matched Image" style="max-width: 300px;"/>
    #         </div>
    #     </div>

    # """
    # return HTMLResponse(content=html_content)


    return templates.TemplateResponse(
        "result.html", 
        {"request": request, "query_image": query_image_base64, "matched_image": matched_image_base64}
    )