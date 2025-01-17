import streamlit as st
from diffusers import DiffusionPipeline
import os 
import streamlit as st
from diffusers import StableDiffusion3Pipeline
from diffusers import StableDiffusionPipeline
import os 
from dotenv import load_dotenv
import torch
load_dotenv()
os.environ["Hugging_Face_Token"] = os.getenv("Hugging_Face_Token")
def generate_image(Body_shape_opt, Body_type_opt, Gender_opt, color_opt):
    # Ensure that the Hugging Face token is set in the environment
    model_id1 = "dreamlike-art/dreamlike-diffusion-1.0"
    model_id2 = "stabilityai/stable-diffusion-xl-base-1.0"
    pipe = StableDiffusionPipeline.from_pretrained(model_id2, torch_dtype=torch.float32, use_safetensors=True)
    pipe = pipe.to("cuda")
    
    # Define the prompt based on the user input
    prompt = f"""Generate a personalized outfit recommendation for:
        Body Shape: {Body_shape_opt}
        Body Type: {Body_type_opt}
        Gender: {Gender_opt}
        Color Complexion: {color_opt}
        Provide a stylish, flattering look with a detailed description of:

        Top wear: Fit and color
        Bottom wear: Design and length
        Footwear: Occasion-appropriate
        Accessories: To complete the outfit"""
    
    # Generate the image using the prompt
    image = pipe(prompt).images[0]

    # Display the generated image in Streamlit
    st.image(image, caption="Generated Outfit", use_column_width=True)

    return image


st.title("Personalized Outfit Suggester")

Body_type_opt=st.selectbox("Body Type",("Ectomorph (Lean and slender)","Mesomorph (Muscular and well-built)","Endomorph (Round and soft)"),index=None,placeholder="Select your body type")
st.write("You selected:", Body_type_opt)
Body_shape_opt=st.selectbox("Body Shape",("Apple – Broader upper body, slimmer hips","Pear – Narrow shoulders, wider hips","Hourglass – Balanced curves with a defined waist",
                                       "Rectangle – Straight body, minimal curves","Inverted Triangle – Broad shoulders, narrow hips","Oval – Rounded body, undefined waist"),index=None,placeholder="Select your body shape")
st.write("You selected:", Body_shape_opt)
Gender_opt=st.selectbox("Gender",("Male","Female","Non-binary"),index=None,placeholder="Select your gender type")
st.write("You selected:", Gender_opt)
color_opt=st.selectbox("Color Complexion",("Fair","Light","Medium","Olive","Tan","Brown","Dark"),index=None,placeholder="Select your Color Complexion")
st.write("You selected:", color_opt)
face_img=st.file_uploader("Your Face Image")

if st.button("Generate"):
    image=generate_image(Body_shape_opt,Body_type_opt,Gender_opt,color_opt)
    st.image("generated image",image)



