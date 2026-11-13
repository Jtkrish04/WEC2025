import streamlit as st
import textwrap

st.set_page_config(page_title="E.S.P.E.K.K.A", layout="wide")

st.markdown("""
<style>
h1, h2, h3, h4 {
    font-family: 'Arial', sans-serif;
}
p, li {
    font-family: 'Arial', sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "About", "Meet the Team", "Design" ,"Product Info", "Contact"])


if page == "Home":

    st.markdown(
        """
        <div style='padding:20px;'>
        <h1 style='text-align:center; font-size:42px; letter-spacing:2px;'>E.S.P.E.K.K.A</h1>

        <p style='text-align:center; font-size:18px; max-width:750px; margin:auto; line-height:1.6;'>
        Welcome to Our Autonomous Siege Vehicle Project.<br><br>
        We designed and built a fully autonomous medieval-inspired robot capable of navigating obstacles, 
        following a guided path, identifying a firing zone, and launching a projectile at a castle tower target.<br><br>
        <strong>Our goal:</strong> Bring medieval engineering into the modern age using sensors, control systems, and robotics.<br><br>
        Explore our design, team, and process using the menu on the left.
        </p>
        </div>
        """,
        unsafe_allow_html=True
        
    )
    st.image("WEC2025/pekka.jpg",use_container_width=True)

elif page == "About":

    st.markdown(
        """
        <div style='padding:20px;'>
        <h1 style='text-align:center; font-size:36px;'>About Our Company</h1>

        <p style='text-align:center; font-size:17px; max-width:780px; margin:auto; line-height:1.6;'>
        This project was created for the 2025 Windsor Engineering Competition (WEC) Senior Design category.<br><br>

        The challenge: modernize a medieval siege mechanism using autonomous technology.<br><br>

        Our robot:<br>
        • Follows a taped path using IR sensors<br>
        • Detects and avoids obstacles<br>
        • Identifies the firing zone<br>
        • Stops precisely and fires a safe projectile<br>
        • Operates fully autonomously once started<br><br>

        A blend of mechanical engineering, electronics, and programming merged into one integrated system.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

elif page == "Meet the Team":
    st.title("Meet the Team")

    def team_member(name, role, image):
        col1, col2 = st.columns([1, 6])
        with col1:
            st.image(image, width=120)
        with col2:
            st.markdown(f"<h2 style='margin-bottom:5px;'>{name}</h2>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='color:gray; margin-top:-5px;'>{role}</h4>", unsafe_allow_html=True)

    team_member("Jad Nizam", "CEO", "WEC2025/Jad.jpeg")
    team_member("Ahmad Raheem", "Electrical Lead", "WEC2025/AHMAD.jpeg")
    team_member("Mohammad Nasir", "Mechanical Lead", "WEC2025/MO.jpeg")
    team_member("Jathushan Krishnamohan", "Programming Lead", "WEC2025/JT.jpeg")


elif page == "Design":
    st.title("Design")
    
    html = textwrap.dedent("""\
    <div style='text-align:center; padding:20px;'>
    <p style='font-size:17px; max-width:750px; margin:auto; line-height:1.6;'>
        Our siege vehicle is built around an Arduino-based 4-wheel platform with integrated sensors and a servo-powered launcher.<br>
        The design focuses on reliability, accuracy, and autonomous operation.
    </p>

    <h3 style='margin-top:25px;'>Key Features</h3>

    <ul style='list-style:disc; display:inline-block; text-align:left; font-size:16px; line-height:1.6;'>
        <li>IR Line Sensor Array for lane following</li>
        <li>Ultrasonic Sensor for obstacle and zone detection</li>
        <li>Servo-powered elastic launcher</li>
        <li>State machine control for full autonomy</li>
        <li>Balanced frame for stable motion</li>
        <li>PID-tuned navigation for smooth movement</li>
    </ul>
    </div>
    """)

    st.markdown(html, unsafe_allow_html=True)
    
    st.subheader("Catia Modelling")
    st.image("WEC2025/CatiaDrawing.webp", use_container_width=True)
    st.image("WEC2025/CatiaDrawing1.webp", use_container_width=True)

    st.subheader("Mechanical Design")
    st.image("WEC2025/CatapultDrawing.jpeg", use_container_width=True)

    st.subheader("Finished Slingshot")
    st.image("WEC2025/Slingshot.webp",use_container_width=True)


elif page == "Product Info":
    st.title("Product Information")

    content = textwrap.dedent("""
        <div style='text-align:left; font-size:17px; line-height:1.6; padding:15px; max-width:800px;'>

        <h3 style='font-size:26px;'>Product Specifications</h3>

        <p><strong>Base Platform:</strong><br>
        • ELEGOO Smart Robot Car Kit (chassis, motors, driver, wheels, sensors)</p>

        <p><strong>Dimensions:</strong><br>
        • Fits within 30 cm × 60 cm × 30 cm WEC limit</p>

        <p><strong>Autonomous Features:</strong><br>
        • IR line detection<br>
        • Ultrasonic obstacle sensing<br>
        • Automatic firing-zone recognition<br>
        • Fully autonomous sequence</p>

        <p><strong>Launcher Mechanism:</strong><br>
        • Servo-triggered elastic launcher<br>
        • Safe, low-energy projectile system<br>
        • Adjustable angle for accuracy</p>

        <p><strong>Power & Operation:</strong><br>
        • Powered by ELEGOO onboard battery<br>
        • Smooth, optimized navigation code<br>
        • Modular design for easy calibration</p>

        <p><strong>Performance Highlights:</strong><br>
        • Tuned straight-line travel<br>
        • Highly repeatable shots<br>
        • Precise zone stopping<br>
        • Competition-ready consistency</p>

        <p><strong>Safety & Compliance:</strong><br>
        • All materials are competition-approved<br>
        • No hazardous components<br>
        • Safe projectile requirements met<br>
        • Fully aligned with Senior Design rules</p>

        </div>
    """)

    st.markdown(content, unsafe_allow_html=True)

elif page == "Contact":
    st.title("Contact Us")
    
    name = st.text_input("Your Name")
    email = st.text_input("Email Address")
    message = st.text_area("Write your message")

    if st.button("Submit"):
        st.success("Thank you! Your message has been received.")

    st.write("---")
    st.write("Email: jathushan.krishnamohan@gmail.com") 
    st.write("Location: Canada")
