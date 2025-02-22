import streamlit as st

# Custom CSS for scrollable container
st.markdown("""
    <style>
        .scrollable-container {
            max-height: 600px;  /* Adjust this value to fit your needs */
            overflow-y: scroll;
        }
    </style>
""", unsafe_allow_html=True)

# Content inside the scrollable container
st.markdown('<div class="scrollable-container">', unsafe_allow_html=True)

# Add a Beautiful Title and Heading
st.markdown("""
    <h1 style="text-align: center; color: #2980b9; font-family: 'Arial', sans-serif; font-size: 36px; font-weight: bold;">
        The Eternal Wisdom of the Quran
    </h1>
    <h3 style="text-align: center; color: #34495e; font-family: 'Arial', sans-serif; font-size: 24px;">
        A Divine Guide for All of Humanity
    </h3>
""", unsafe_allow_html=True)

# Using Markdown with HTML for color styling
st.markdown("""
    <p style="color: #2c3e50; font-size: 18px;">
        The <strong style="color: #e74c3c;">Quran</strong> is the eternal and divine scripture of Islam, a radiant beacon of light 
        that has guided humanity for over 1,400 years. Revealed to the Prophet Muhammad (PBUH) over 23 years, it is a testament to the 
        infinite wisdom and mercy of Allah. With its 114 chapters (Surahs) and over 6,000 verses (Ayahs), it provides profound guidance 
        on matters of faith, morality, social justice, and personal conduct. Every word in the Quran is a call to reflection, an invitation 
        to live in harmony with the Creator and with creation, emphasizing the oneness of Allah, the certainty of the Day of Judgment, and 
        the principles of compassion, kindness, and truth. The Quran remains preserved in its original form, unchanged since its revelation, 
        offering timeless wisdom for those who seek peace, clarity, and righteousness in their lives.
    </p>
""", unsafe_allow_html=True)


# Styling the title
st.markdown("""
    <h1 style="text-align: center; font-family: 'Arial', sans-serif; font-size: 48px; font-weight: bold; color: #8e44ad;">
        Islamic Resource Center
    </h1>
""", unsafe_allow_html=True)

# Styling the text
st.markdown("""
    <p style="font-size: 24px; font-weight: bold; color: #e74c3c; text-align: center;">
        View & Read the <span style="color: #2980b9;">Quran</span> PDF
    </p>
""", unsafe_allow_html=True)

webpage_urly = 'https://www.islamicnet.com/quran.php'
st.markdown(f'<iframe src="{webpage_urly}" width="800" height="600"></iframe>', unsafe_allow_html=True)

st.write("Quran MP3 Files")
webpage_url = 'https://quranicaudio.com/'
st.markdown(f'<iframe src="{webpage_url}" width="800" height="600"></iframe>', unsafe_allow_html=True)


# Styling the text
st.markdown("""
    <p style="font-size: 24px; font-weight: bold; color: #27ae60; text-align: center;">
        Full <span style="color: #8e44ad;">Quran</span> Recitation <span style="color: #f39c12;">Videos</span>
    </p>
""", unsafe_allow_html=True)

# CSS to center-align the table and apply some styling
st.markdown("""
    <style>
        table {
            margin-left: auto;
            margin-right: auto;
            width: 80%;
            text-align: center;
            border-collapse: collapse;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ddd;
        }
        th {
            background-color: #f2f2f2;
        }
        td a {
            color: #1a73e8;
            text-decoration: none;
        }
        td a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Table with all 114 links
st.markdown("""
    <table>
        <tr><th>Surah Number</th><th>Surah Name</th><th>Link</th></tr>
        <tr><td>1</td><td>Surah Al-Fatiha</td><td><a href="https://youtu.be/u1nqafqyqTA?feature=shared">Watch</a></td></tr>
        <tr><td>2</td><td>Surah Al-Baqara</td><td><a href="https://youtu.be/nibOG3vRGpU?feature=shared">Watch</a></td></tr>
        <tr><td>3</td><td>Surah Aali Imran</td><td><a href="https://youtu.be/tf26W_1mdFg?feature=shared">Watch</a></td></tr>
        <tr><td>4</td><td>Surah An-Nisa</td><td><a href="https://youtu.be/G0NqWjlXlQE?feature=shared">Watch</a></td></tr>
        <tr><td>5</td><td>Surah Al-Ma’idah</td><td><a href="https://youtu.be/EFgAy0OP7CM?feature=shared">Watch</a></td></tr>
        <!-- Add the remaining rows here -->
    </table>
""", unsafe_allow_html=True)
        
st.markdown('</div>', unsafe_allow_html=True)


