import streamlit as st
import base64
from datetime import datetime
import pytz
import streamlit.components.v1 as components

def main():
    st.markdown("<h1 style='text-align: center; margin-bottom: 20px; margin-left: 60px;'>Who am I?</h1>", unsafe_allow_html=True)
    
    # Add an image from a local file in a rounded frame with name in a div matching Streamlit's background
    image_path = "pics/picture.jpg"
    st.markdown(
        f"""
        <div style="display: flex; align-items: center;">
            <div style="
                border-radius: 15px;
                overflow: hidden;
                width: 200px;
                border: 2px solid #ccc;
                margin-right: 20px;
                margin-left: 80px;
            ">
                <img src="data:image/png;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}" width="200">
            </div>
            <div style="display: flex; flex-direction: column;">
                <div style="
                    background-color: pink;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(255, 192, 203, 0.5);
                    margin-bottom: 10px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                ">
                    <p style="margin: 0; padding: 0; color: #ffffff; text-align: center; font-size: 2em; font-weight: bold;">Aliza May Bataluna</p>
                </div>
                <p style="margin: 0; padding: 0; color: #ffffff;">Bachelor of Science in Information Technology</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
        # Add "My birthday is" section with countdown timer
    countdown_html = """
    <div style='
        font-family: "Source Sans Pro", sans-serif;
        background-color: #0e1117;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 3);
        margin: 30px auto;
        max-width: 600px;
        
    '>
        <p style='text-align: center; font-size: 1.5em; font-weight: bold; color: #ffffff; margin-bottom: 10px;'>My birthday is <span style='color: pink;'>May 3, 2002</span></p>
        <p style='text-align: center; font-size: 1.2em; color: #ffffff; margin-bottom: 15px;'>Countdown to next birthday:</p>
        <div style='
            background-color: #0e1117;
            border-radius: 15px;
            padding: 20px;
            margin: 0 auto;
            max-width: 500px;
        '>
            <div id='countdown' style='display: flex; justify-content: center; text-align: center;'>
                <div style='margin: 0 10px;'>
                    <div style='background-color: white; border-radius: 10px; padding: 10px; margin-bottom: 5px;'>
                        <span id='days' style='font-size: 1.5em; font-weight: bold; color: #0e1117;'></span>
                    </div>
                    <span style='color: #ffffff;'>Days</span>
                </div>
                <div style='margin: 0 10px;'>
                    <div style='background-color: white; border-radius: 10px; padding: 10px; margin-bottom: 5px;'>
                        <span id='hours' style='font-size: 1.5em; font-weight: bold; color: #0e1117;'></span>
                    </div>
                    <span style='color: #ffffff;'>Hours</span>
                </div>
                <div style='margin: 0 10px;'>
                    <div style='background-color: white; border-radius: 10px; padding: 10px; margin-bottom: 5px;'>
                        <span id='minutes' style='font-size: 1.5em; font-weight: bold; color: #0e1117;'></span>
                    </div>
                    <span style='color: #ffffff;'>Minutes</span>
                </div>
                <div style='margin: 0 10px;'>
                    <div style='background-color: white; border-radius: 10px; padding: 10px; margin-bottom: 5px;'>
                        <span id='seconds' style='font-size: 1.5em; font-weight: bold; color: #0e1117;'></span>
                    </div>
                    <span style='color: #ffffff;'>Seconds</span>
                </div>
            </div>
        </div>
    </div>
    <script>
    function updateCountdown() {
        const now = new Date();
        const birthday = new Date(now.getFullYear(), 4, 3); // May is month 4 (0-indexed)
        if (now > birthday) {
            birthday.setFullYear(birthday.getFullYear() + 1);
        }
        const timeLeft = birthday - now;
        
        const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);
        
        document.getElementById('days').textContent = days;
        document.getElementById('hours').textContent = hours;
        document.getElementById('minutes').textContent = minutes;
        document.getElementById('seconds').textContent = seconds;
    }
    
    updateCountdown();
    setInterval(updateCountdown, 1000);
    </script>
    """
    
    components.html(countdown_html, height=300)
    
    st.markdown("<h2 style='text-align: center; margin-top: 0px;'>I am a/an...</h2>", unsafe_allow_html=True)

    # Function to encode the image
    def img_to_base64(img_path):
        with open(img_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')

    # Encode the image
    taurus = img_to_base64("pics/taurus.png")
    istj = img_to_base64("pics/istj.png")
    gamer = img_to_base64("pics/gamer.png")
    dog = img_to_base64("pics/dog.png")
    anime = img_to_base64("pics/anime.png")
    book = img_to_base64("pics/book.png")
    music = img_to_base64("pics/music.png")
    pink = img_to_base64("pics/pink.png")
    froyo = img_to_base64("pics/froyo.png")

    # Create a 3x3 grid of divs with rounded corners, drop shadows, and hover effects
    grid_html = """
    <style>
        .grid-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
            margin-top: 10px;
        }
        .grid-item {
            background-color: #0e1117;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 3);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 150px;
            font-size: 24px;
            font-weight: bold;
            transition: background-color 0.3s ease;
            cursor: pointer;
            flex-direction: column;
            padding-top: 20px;
        }
        .grid-item:hover {
            background-color: #e0e0e0;
        }
        .grid-item img {
            max-width: 100%;
            max-height: 70%;
            object-fit: contain;
        }
    </style>
    <div class="grid-container">
    """

    for i in range(1, 10):
        if i == 1:
            grid_html += f'<div class="grid-item"><img src="data:image/png;base64,{taurus}" alt="Taurus"><p>Taurus</p></div>'
        elif i == 2:
            grid_html += f'<div class="grid-item"><img src="data:image/png;base64,{istj}" alt="ISTJ"><p>ISTJ</p></div>'
        elif i == 3:
            grid_html += f'<div class="grid-item"><img src="data:image/png;base64,{gamer}" alt="Gamer"><p>Gamer</p></div>'
        elif i == 4:
            grid_html += f'<div class="grid-item"><img src="data:image/png;base64,{dog}" alt="Dog"><p>Dog lover</p></div>'
        elif i == 5:
            grid_html += f'<div class="grid-item"><img src="data:image/png;base64,{anime}" alt="Pokemon"><p>Anime fan</p></div>'
        elif i == 6:
            grid_html += f'<div class="grid-item"><img src="data:image/png;base64,{book}" alt="Book"><p>Bookworm</p></div>'
        elif i == 7:
            grid_html += f'<div class="grid-item"><img src="data:image/png;base64,{music}" alt="Music"><p>Music lover</p></div>'
        elif i == 8:
            grid_html += f'<div class="grid-item"><img src="data:image/png;base64,{pink}" alt="Pink"><p>Pink lover</p></div>'
        elif i == 9:
            grid_html += f'<div class="grid-item"><img src="data:image/png;base64,{froyo}" alt="Froyo"><p>Froyo enjoyer</p></div>'
        else:
            grid_html += f'<div class="grid-item">{i}</div>'

    grid_html += "</div>"

    st.markdown(grid_html, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center; margin-top: 40px;'>Let's socialize!</h3>", unsafe_allow_html=True)

    # Function to encode the image
    def img_to_base64(img_path):
        with open(img_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')

    # Encode the GitHub icon
    github_icon = img_to_base64("pics/github.png")
    linkedin_icon = img_to_base64("pics/linkedin.png")
    facebook_icon = img_to_base64("pics/facebook.png")

    # Add the new 3x2 grid
    socialize_grid_html = """
    <style>
        .socialize-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
            margin-top: 20px;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }
        .socialize-item {
            background-color: #0e1117;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 50px;
            font-size: 20px;
            font-weight: bold;
            color: #ffffff;
            transition: background-color 0.3s ease, color 0.3s ease;
            cursor: pointer;
            text-decoration: none;
        }
        .socialize-item:hover {
            background-color: #e0e0e0;
            color: #0e1117;
        }
        .socialize-item img {
            width: 30px;
            height: 30px;
            margin-right: 10px;
        }
        .socialize-item span {
            color: white;
        }
    </style>
    <div class="socialize-grid">
    """

    for i in range(1, 7):
        if i == 1:
            socialize_grid_html += f'<a href="https://github.com/alizamayyy" target="_blank" class="socialize-item"><img src="data:image/png;base64,{github_icon}" alt="GitHub"><span>GitHub</span></a>'
        elif i == 2:
            socialize_grid_html += f'<a href="https://www.linkedin.com/in/alizabataluna/" target="_blank" class="socialize-item"><img src="data:image/png;base64,{linkedin_icon}" alt="LinkedIn"><span>LinkedIn</span></a>'
        elif i == 3:
            socialize_grid_html += f'<a href="https://www.facebook.com/lizalizalizaaa/" target="_blank" class="socialize-item"><img src="data:image/png;base64,{facebook_icon}" alt="Facebook"><span>Facebook</span></a>'

    socialize_grid_html += "</div>"

    st.markdown(socialize_grid_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()