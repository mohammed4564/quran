import streamlit as st
import pandas as pd

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
        The Everlasting Wisdom of the Quran: A Guide to Truth and Light
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

# Styling the text
st.markdown("""
    <p style="font-size: 24px; font-weight: bold; color: #27ae60; text-align: center;">
        Download <span style="color: #8e44ad;">And</span> Read <span style="color: #f39c12;">quran</span>
    </p>
""", unsafe_allow_html=True)

# GitHub repository URL for the raw files
github_repo_url = 'https://raw.githubusercontent.com/mohammed4564/quran/main/.devcontainer/'

# List of Para numbers with their corresponding names in Arabic and English
pdf_files = [
    {"name": "Para 1: Al-Fatiha", "arabic_name": "الفاتحة", "file": "Holy-Quran-Para-1.pdf"},
    {"name": "Para 2: Al-Baqarah", "arabic_name": "البقرة", "file": "Holy-Quran-Para-2.pdf"},
    {"name": "Para 3: Aal-E-Imran", "arabic_name": "آل عمران", "file": "Holy-Quran-Para-3.pdf"},
    {"name": "Para 4: An-Nisa", "arabic_name": "النساء", "file": "Holy-Quran-Para-4.pdf"},
    {"name": "Para 5: Al-Ma'idah", "arabic_name": "المائدة", "file": "Holy-Quran-Para-5.pdf"},
    {"name": "Para 6: Al-An'am", "arabic_name": "الأنعام", "file": "Holy-Quran-Para-6.pdf"},
    {"name": "Para 7: Al-A'raf", "arabic_name": "الأعراف", "file": "Holy-Quran-Para-7.pdf"},
    {"name": "Para 8: Al-Anfal", "arabic_name": "الأنفال", "file": "Holy-Quran-Para-8.pdf"},
    {"name": "Para 9: At-Tawbah", "arabic_name": "التوبة", "file": "Holy-Quran-Para-9.pdf"},
    {"name": "Para 10: Yunus", "arabic_name": "يونس", "file": "Holy-Quran-Para-10.pdf"},
    {"name": "Para 11: Hud", "arabic_name": "هود", "file": "Holy-Quran-Para-11.pdf"},
    {"name": "Para 12: Yusuf", "arabic_name": "يوسف", "file": "Holy-Quran-Para-12.pdf"},
    {"name": "Para 13: Ibrahim", "arabic_name": "إبراهيم", "file": "Holy-Quran-Para-13.pdf"},
    {"name": "Para 14: Al-Hijr", "arabic_name": "الحجر", "file": "Holy-Quran-Para-14.pdf"},
    {"name": "Para 15: An-Nahl", "arabic_name": "النحل", "file": "Holy-Quran-Para-15.pdf"},
    {"name": "Para 16: Al-Isra", "arabic_name": "الإسراء", "file": "Holy-Quran-Para-16.pdf"},
    {"name": "Para 17: Al-Kahf", "arabic_name": "الكهف", "file": "Holy-Quran-Para-17.pdf"},
    {"name": "Para 18: Maryam", "arabic_name": "مريم", "file": "Holy-Quran-Para-18.pdf"},
    {"name": "Para 19: Ta-Ha", "arabic_name": "طه", "file": "Holy-Quran-Para-19.pdf"},
    {"name": "Para 20: Al-Anbiya", "arabic_name": "الأنبياء", "file": "Holy-Quran-Para-20.pdf"},
    {"name": "Para 21: Al-Hajj", "arabic_name": "الحج", "file": "Holy-Quran-Para-21.pdf"},
    {"name": "Para 22: Al-Mu'minun", "arabic_name": "المؤمنون", "file": "Holy-Quran-Para-22.pdf"},
    {"name": "Para 23: An-Nur", "arabic_name": "النور", "file": "Holy-Quran-Para-23.pdf"},
    {"name": "Para 24: Al-Furqan", "arabic_name": "الفرقان", "file": "Holy-Quran-Para-24.pdf"},
    {"name": "Para 25: Ash-Shu'ara", "arabic_name": "الشعراء", "file": "Holy-Quran-Para-25.pdf"},
    {"name": "Para 26: An-Naml", "arabic_name": "النمل", "file": "Holy-Quran-Para-26.pdf"},
    {"name": "Para 27: Al-Ahqaf", "arabic_name": "الأحقاف", "file": "Holy-Quran-Para-27.pdf"},
    {"name": "Para 28: Az-Zariyat", "arabic_name": "الذاريات", "file": "Holy-Quran-Para-28.pdf"},
    {"name": "Para 29: Al-Mujadila", "arabic_name": "المجادلة", "file": "Holy-Quran-Para-29.pdf"},
    {"name": "Para 30: Al-Buruj", "arabic_name": "البروج", "file": "Holy-Quran-Para-30.pdf"}
]

# Create a DataFrame for the table
df = pd.DataFrame(pdf_files)

# Table structure with styles and icons
st.markdown("""
    <style>
        table {
            margin-left: auto;
            margin-right: auto;
            width: 90%;
            text-align: center;
            border-collapse: collapse;
        }
        th, td {
            padding: 12px;
            text-align: center;
            border: 1px solid #ddd;
            min-width: 250px;  /* Ensure columns have a fixed minimum width */
        }
        th {
            background-color: #f4f4f4;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        tr:nth-child(odd) {
            background-color: #e9f7ef;
        }
        .download-btn {
            color: #007BFF;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .download-btn:hover {
            text-decoration: underline;
        }
        .pdf-icon {
            margin-right: 10px;  /* Adds space between icon and text */
        }

        /* Reduce the width of the Sl. No. column */
        td:first-child, th:first-child {
            min-width: 70px;  /* Reduce width of the first column (Sl. No.) */
        }
    </style>
    <table>
        <tbody>
""", unsafe_allow_html=True)

# Add the first row (column names as part of data)
st.markdown(f"""
    <tr>
        <td><strong>Sl. No.</strong></td>
        <td><strong>Para Name</strong></td>
        <td><strong>Download PDF</strong></td>
    </tr>
""", unsafe_allow_html=True)

# Populate the table with data
for index, row in df.iterrows():
    para_name = row['name']
    pdf_url = f"{github_repo_url}{row['file']}"
    sl_no = index + 1  # Sl. No. starting from 1

    # Adding rows to the table with PDF icon and download button
    st.markdown(f"""
        <tr>
            <td>{sl_no}</td>
            <td>{para_name} ({row['arabic_name']})</td>
            <td>
                <a href="{pdf_url}" target="_blank" class="download-btn">
                    <i class="fas fa-file-pdf pdf-icon"></i> Download PDF
                </a>
            </td>
        </tr>
    """, unsafe_allow_html=True)

# Closing the table properly
st.markdown("""
        </tbody>
    </table>
""", unsafe_allow_html=True)
###########################################################################################################################
import streamlit as st
import pandas as pd

# List of your MP3 files
mp3_files = [
    "001-al-fatihah.mp3", "002-al-baqarah.mp3", "003-al-imran.mp3", "004-an-nisa.mp3",
    "005-al-maidah.mp3", "006-al-anam.mp3", "007-al-araf.mp3", "008-al-anfal.mp3",
    "009-at-taubah.mp3", "010-yunus.mp3", "011-hud.mp3", "012-yusuf.mp3", "013-ar-rad.mp3",
    "014-ibrahim.mp3", "015-al-hijr.mp3", "016-an-nahl.mp3", "017-al-isra.mp3", "018-al-kahf.mp3",
    "019-maryam.mp3", "020-ta-ha.mp3", "021-al-anbiya.mp3", "022-al-hajj.mp3", "023-al-muminun.mp3",
    "024-an-nur.mp3", "025-al-furqan.mp3", "026-ash-shuara.mp3", "027-an-naml.mp3", "028-al-qasas.mp3",
    "029-al-ankabut.mp3", "030-ar-rum.mp3", "031-luqman.mp3", "032-as-sajdah.mp3", "033-al-ahzab.mp3",
    "034-saba.mp3", "035-fatir.mp3", "036-ya-sin.mp3", "037-as-saffat.mp3", "038-sad.mp3", "039-az-zumar.mp3",
    "040-ghafir.mp3", "041-fussilat.mp3", "042-ash-shura.mp3", "043-az-zukhruf.mp3", "044-ad-dukhan.mp3",
    "045-al-jathiyah.mp3", "046-al-ahqaf.mp3", "047-muhammad.mp3", "048-al-fath.mp3", "049-al-hujurat.mp3",
    "050-qaf.mp3", "051-adh-dhariyat.mp3", "052-at-tur.mp3", "053-an-najm.mp3", "054-al-qamar.mp3",
    "055-ar-rahman.mp3", "056-al-waqiah.mp3", "057-al-hadid.mp3", "058-al-mujadilah.mp3", "059-al-hashr.mp3",
    "060-al-mumtahanah.mp3", "061-as-saff.mp3", "062-al-jumuah.mp3", "063-al-munafiqun.mp3", "064-at-taghabun.mp3",
    "065-at-talaq.mp3", "066-at-tahrim.mp3", "067-al-mulk.mp3", "068-al-qalam.mp3", "069-al-haqqah.mp3",
    "070-al-maarij.mp3", "071-nuh.mp3", "072-al-jinn.mp3", "073-al-muzammil.mp3", "074-al-muddaththir.mp3",
    "075-al-qiyamah.mp3", "076-al-insan.mp3", "077-al-mursalat.mp3", "078-an-naba.mp3", "079-an-naziat.mp3",
    "080-abasa.mp3", "081-at-takwir.mp3", "082-al-infitar.mp3", "083-al-mutaffifin.mp3", "084-al-inshiqaq.mp3",
    "085-al-buruj.mp3", "086-at-tariq.mp3", "087-al-ala.mp3", "088-al-ghashiyah.mp3", "089-al-fajr.mp3",
    "090-al-balad.mp3", "091-ash-shams.mp3", "092-al-lail.mp3", "093-ad-duha.mp3", "094-ash-sharh.mp3",
    "095-at-tin.mp3", "096-al-alaq.mp3", "097-al-qadr.mp3", "098-al-baiyyinah.mp3", "099-az-zalzalah.mp3",
    "100-al-adiyat.mp3", "101-al-qariah.mp3", "102-at-takathur.mp3", "103-al-asr.mp3", "104-al-humazah.mp3",
    "105-al-fil.mp3", "106-quraish.mp3", "107-al-maun.mp3", "108-al-kauthar.mp3", "109-al-kafirun.mp3",
    "110-an-nasr.mp3", "111-al-masad.mp3", "112-al-ikhlas.mp3", "113-al-falaq.mp3", "114-an-nas.mp3"
]

# Generate Surah names based on MP3 file names
surah_names = [f"Surah {i+1} ({mp3.split('-')[1].split('.')[0]})" for i, mp3 in enumerate(mp3_files)]

# Create a DataFrame
data = {
    'Sl. No': list(range(1, len(mp3_files)+1)),
    'Surah Name': surah_names,
    'Audio': mp3_files
}

df = pd.DataFrame(data)

# Display the DataFrame as a table in Streamlit
st.title("Quran Audio Table")

# Loop to display each row with a play button
for index, row in df.iterrows():
    surah_name = row['Surah Name']
    mp3_file = row['Audio']
    
    # Display the row
    st.write(f"{row['Sl. No']}. {surah_name}")

    # Add play button for each audio file
    if st.button(f"Play {surah_name}"):
        st.audio(mp3_file)

    st.write("")  # Adding space between each row for better readability

#############################################################################################################################
# Styling the text
st.markdown("""
    <p style="font-size: 24px; font-weight: bold; color: #27ae60; text-align: center;">
        Full <span style="color: #8e44ad;">Quran</span> Recitation <span style="color: #f39c12;">Videos</span>
    </p>
""", unsafe_allow_html=True)

#CSS to center-align the table and apply some styling
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

#Updated table with target="_blank" added to each link
st.markdown("""
     <table>
        <tr><th>Surah Number</th><th>Surah Name</th><th>Link</th></tr>
        <tr><td>1</td><td>Surah Al-Fatiha</td><td><a href="https://youtu.be/UDvh63xHVa0?feature=shared">Watch</a></td></tr>
        <tr><td>2</td><td>Surah Al-Baqara</td><td><a href="https://youtu.be/8x_URBJW5Dk?feature=shared">Watch</a></td></tr>
        <tr><td>3</td><td>Surah Aali Imran</td><td><a href="https://youtu.be/mNqoSW_5SmA?feature=shared">Watch</a></td></tr>
        <tr><td>4</td><td>Surah An-Nisa</td><td><a href="https://youtu.be/fMo163Ya3SY?feature=shared">Watch</a></td></tr>
        <tr><td>5</td><td>Surah Al-Ma’idah</td><td><a href="https://youtu.be/9zqVkeoAP7U?feature=shared">Watch</a></td></tr>
        <tr><td>6</td><td>Surah Al-An’am</td><td><a href="https://youtu.be/liK3RH8f8QA?feature=shared">Watch</a></td></tr>
        <tr><td>7</td><td>Surah Al-A’raf</td><td><a href="https://youtu.be/_JFNbs6IUgU?feature=shared">Watch</a></td></tr>
        <tr><td>8</td><td>Surah Al-Anfal</td><td><a href="https://youtu.be/3fDDtUnvta8?feature=shared">Watch</a></td></tr>
        <tr><td>9</td><td>Surah At-Tawbah</td><td><a href="https://youtu.be/QJVuFqXxLo4?feature=shared">Watch</a></td></tr>
        <tr><td>10</td><td>Surah Yunus</td><td><a href="https://youtu.be/GcA0hs9Ornk?feature=shared">Watch</a></td></tr>
        <tr><td>11</td><td>Surah Hud</td><td><a href="https://youtu.be/Cs24aEm0q3o?feature=shared">Watch</a></td></tr>
        <tr><td>12</td><td>Surah Yusuf</td><td><a href="https://youtu.be/oTRSrJM0WAM?feature=shared">Watch</a></td></tr>
        <tr><td>13</td><td>Surah Ar-Ra’d</td><td><a href="https://youtu.be/gfAdREN1SL8?feature=shared">Watch</a></td></tr>
        <tr><td>14</td><td>Surah Ibrahim</td><td><a href="https://youtu.be/vH2AhmUSQ74?feature=shared">Watch</a></td></tr>
        <tr><td>15</td><td>Surah Al-Hijr</td><td><a href="https://youtu.be/zevi4w8cv_0?feature=shared">Watch</a></td></tr>
        <tr><td>16</td><td>Surah An-Nahl</td><td><a href="https://youtu.be/jw_MvrLWJ6A?feature=shared">Watch</a></td></tr>
        <tr><td>17</td><td>Surah Al-Isra</td><td><a href="https://youtu.be/OJccFa-kVfM?feature=shared">Watch</a></td></tr>
        <tr><td>18</td><td>Surah Al-Kahf</td><td><a href="https://youtu.be/ozHal4UUXl0?feature=shared">Watch</a></td></tr>
        <tr><td>19</td><td>Surah Maryam</td><td><a href="https://youtu.be/huSrUH-spDw?feature=shared">Watch</a></td></tr>
        <tr><td>20</td><td>Surah Taha</td><td><a href="https://youtu.be/pn7pwU7U-kk?feature=shared">Watch</a></td></tr>
        <tr><td>21</td><td>Surah Al-Anbiya</td><td><a href="https://youtu.be/NUIKzCabZfA?feature=shared">Watch</a></td></tr>
        <tr><td>22</td><td>Surah Al-Hajj</td><td><a href="https://youtu.be/aXtz3-4EOds?feature=shared">Watch</a></td></tr>
        <tr><td>23</td><td>Surah Al-Mu’minun</td><td><a href="https://youtu.be/D1RL-lQZuqQ?feature=shared">Watch</a></td></tr>
        <tr><td>24</td><td>Surah An-Nur</td><td><a href="https://youtu.be/vzfITR_YabY?feature=shared">Watch</a></td></tr>
        <tr><td>25</td><td>Surah Al-Furqan</td><td><a href="https://youtu.be/mNbAc2ebg7A?feature=shared">Watch</a></td></tr>
        <tr><td>26</td><td>Surah Ash-Shu’ara</td><td><a href="https://youtu.be/4ZaPUeVM0tM?feature=shared">Watch</a></td></tr>
        <tr><td>27</td><td>Surah An-Naml</td><td><a href="https://youtu.be/LcKpQPK9QrE?feature=shared">Watch</a></td></tr>
        <tr><td>28</td><td>Surah Al-Qasas</td><td><a href="https://youtu.be/YJOFzpK4XTE?feature=shared">Watch</a></td></tr>
        <tr><td>29</td><td>Surah Al-Ankabut</td><td><a href="https://youtu.be/z9fD6P4yhOs?feature=shared">Watch</a></td></tr>
        <tr><td>30</td><td>Surah Ar-Rum</td><td><a href="https://youtu.be/pXhar6aJmaY?feature=shared">Watch</a></td></tr>
        <tr><td>31</td><td>Surah Luqman</td><td><a href="https://youtu.be/ND5QWd7MB70?feature=shared">Watch</a></td></tr>
        <tr><td>32</td><td>Surah As-Sajdah</td><td><a href="https://youtu.be/NQ6hyyjlq7c?feature=shared">Watch</a></td></tr>
        <tr><td>33</td><td>Surah Al-Ahzab</td><td><a href="https://youtu.be/vybruxcWZTs?feature=shared">Watch</a></td></tr>
        <tr><td>34</td><td>Surah Saba</td><td><a href="https://youtu.be/atLcGsBXqdE?feature=shared">Watch</a></td></tr>
        <tr><td>35</td><td>Surah Fatir</td><td><a href="https://youtu.be/DQKIBzLkkzc?feature=shared">Watch</a></td></tr>
        <tr><td>36</td><td>Surah Yaseen</td><td><a href="https://youtu.be/Q9xYG8PLxeg?feature=shared">Watch</a></td></tr>
        <tr><td>37</td><td>Surah As-Saffat</td><td><a href="https://youtu.be/Al0b4T3uqro?feature=shared">Watch</a></td></tr>
        <tr><td>38</td><td>Surah Sad</td><td><a href="https://youtu.be/ZA4o73IpYFw?feature=shared">Watch</a></td></tr>
        <tr><td>39</td><td>Surah Az-Zumar</td><td><a href="https://youtu.be/HpiZrGTPGjw?feature=shared">Watch</a></td></tr>
        <tr><td>40</td><td>Surah Ghafir</td><td><a href="https://youtu.be/fQfksWKINk4?feature=shared">Watch</a></td></tr>
        <tr><td>41</td><td>Surah Fussilat</td><td><a href="https://youtu.be/Vx7EKm90hSA?feature=shared">Watch</a></td></tr>
        <tr><td>42</td><td>Surah Ash-Shura</td><td><a href="https://youtu.be/Q8Q16INbLe8?feature=shared">Watch</a></td></tr>
        <tr><td>43</td><td>Surah Az-Zukhruf</td><td><a href="https://youtu.be/K-DYuUuN61U?feature=shared">Watch</a></td></tr>
        <tr><td>44</td><td>Surah Ad-Dukhan</td><td><a href="https://youtu.be/QvLqDAECum8?feature=shared">Watch</a></td></tr>
        <tr><td>45</td><td>Surah Al-Jathiya</td><td><a href="https://youtu.be/u7ZQCWzGTh8?feature=shared">Watch</a></td></tr>
        <tr><td>46</td><td>Surah Al-Ahqaf</td><td><a href="https://youtu.be/FRbqhz12L9o?feature=shared">Watch</a></td></tr>
        <tr><td>47</td><td>Surah Muhammad</td><td><a href="https://youtu.be/yD7gNwi4esQ?feature=shared">Watch</a></td></tr>
        <tr><td>48</td><td>Surah Al-Fath</td><td><a href="https://youtu.be/On9rhT1Iw0U?feature=shared">Watch</a></td></tr>
        <tr><td>49</td><td>Surah Al-Hujurat</td><td><a href="https://youtu.be/viHOv8Hspis?feature=shared">Watch</a></td></tr>
        <tr><td>50</td><td>Surah Qaf</td><td><a href="https://youtu.be/um7O7iuvXzY?feature=shared">Watch</a></td></tr>
        <tr><td>51</td><td>Surah Adh-Dhariyat</td><td><a href="https://youtu.be/kRrkXBdPLDQ?feature=shared">Watch</a></td></tr>
        <tr><td>52</td><td>Surah At-Tur</td><td><a href="https://youtu.be/5SI5NAEbhbo?feature=shared">Watch</a></td></tr>
        <tr><td>53</td><td>Surah An-Najm</td><td><a href="https://youtu.be/6eIPNa1VZyU?feature=shared">Watch</a></td></tr>
        <tr><td>54</td><td>Surah Al-Qamar</td><td><a href="https://youtu.be/C7tPyQVWh5Q?feature=shared">Watch</a></td></tr>
        <tr><td>55</td><td>Surah Ar-Rahman</td><td><a href="https://youtu.be/q--zAOMtQE4?feature=shared">Watch</a></td></tr>
        <tr><td>56</td><td>Surah Al-Waqi’ah</td><td><a href="https://youtu.be/pRxe3IDhzWI?feature=shared">Watch</a></td></tr>
        <tr><td>57</td><td>Surah Al-Hadid</td><td><a href="https://youtu.be/amUiwxHQ8Iw?feature=shared">Watch</a></td></tr>
        <tr><td>58</td><td>Surah Al-Mujadila</td><td><a href="https://youtu.be/GaDJ8-BKqr0?feature=shared">Watch</a></td></tr>
        <tr><td>59</td><td>Surah Al-Hashr</td><td><a href="https://youtu.be/cbwec9puSug?feature=shared">Watch</a></td></tr>
        <tr><td>60</td><td>Surah Al-Mumtahina</td><td><a href="https://youtu.be/gKB7TJ7_vNo?feature=shared">Watch</a></td></tr>
        <tr><td>61</td><td>Surah As-Saff</td><td><a href="https://youtu.be/2ermATsCofM?feature=shared">Watch</a></td></tr>
        <tr><td>62</td><td>Surah Al-Jumu’a</td><td><a href="https://youtu.be/kNS_xapmyWo?feature=shared">Watch</a></td></tr>
        <tr><td>63</td><td>Surah Al-Munafiqun</td><td><a href="https://youtu.be/hcfHY0vPxXU?feature=shared">Watch</a></td></tr>
        <tr><td>64</td><td>Surah At-Taghabun</td><td><a href="https://youtu.be/ILfO_61wxqU?feature=shared">Watch</a></td></tr>
        <tr><td>65</td><td>Surah At-Talaq</td><td><a href="https://youtu.be/eog2u7jigzo?feature=shared">Watch</a></td></tr>
        <tr><td>66</td><td>Surah At-Tahrim</td><td><a href="https://youtu.be/RO3JGHqieN0?feature=shared">Watch</a></td></tr>
        <tr><td>67</td><td>Surah Al-Mulk</td><td><a href="https://youtu.be/9WyZl9FxREY?feature=shared">Watch</a></td></tr>
        <tr><td>68</td><td>Surah Al-Qalam</td><td><a href="https://youtu.be/otudaLjZBuY?feature=shared">Watch</a></td></tr>
        <tr><td>69</td><td>Surah Al-Haqqah</td><td><a href="https://youtu.be/FtsmJMz8AYw?feature=shared">Watch</a></td></tr>
        <tr><td>70</td><td>Surah Al-Maarij</td><td><a href="https://youtu.be/ai30YF3AGb4?feature=shared">Watch</a></td></tr>
        <tr><td>71</td><td>Surah Nuh</td><td><a href="https://youtu.be/O61XEc4fBkY?feature=shared">Watch</a></td></tr>
        <tr><td>72</td><td>Surah Al-Jinn</td><td><a href="https://youtu.be/VhFW2th-iIo?feature=shared">Watch</a></td></tr>
        <tr><td>73</td><td>Surah Al-Muzzammil</td><td><a href="https://youtu.be/wawkeiueSBk?feature=shared">Watch</a></td></tr>
        <tr><td>74</td><td>Surah Al-Muddathir</td><td><a href="https://youtu.be/Nhl0AZQaa_g?feature=shared">Watch</a></td></tr>
        <tr><td>75</td><td>Surah Al-Qiyamah</td><td><a href="https://youtu.be/6evCVJmerJs?feature=shared">Watch</a></td></tr>
        <tr><td>76</td><td>Surah Al-Insan</td><td><a href="https://youtu.be/QOUp0GmgCQg?feature=shared">Watch</a></td></tr>
        <tr><td>77</td><td>Surah Al-Mursalat</td><td><a href="https://youtu.be/Uc0XgRE7718?feature=shared">Watch</a></td></tr>
        <tr><td>78</td><td>Surah An-Naba</td><td><a href="https://youtu.be/uPI5vmuI8WY?feature=shared">Watch</a></td></tr>
        <tr><td>79</td><td>Surah An-Nazi’at</td><td><a href="https://youtu.be/oyahCibEdVE?feature=shared">Watch</a></td></tr>
        <tr><td>80</td><td>Surah Abasa</td><td><a href="https://youtu.be/K7H5DG5-6no?feature=shared">Watch</a></td></tr>
        <tr><td>81</td><td>Surah At-Takwir</td><td><a href="https://youtu.be/2l5gZctbgcE?feature=shared">Watch</a></td></tr>
        <tr><td>82</td><td>Surah Al-Infitar</td><td><a href="https://youtu.be/Y2NEO3LDec8?feature=shared">Watch</a></td></tr>
        <tr><td>83</td><td>Surah Al-Mutaffifin</td><td><a href="https://youtu.be/3bVJMONwoAw?feature=shared">Watch</a></td></tr>
        <tr><td>84</td><td>Surah Al-Inshiqaq</td><td><a href="https://youtu.be/cd4HW9rJLpI?feature=shared">Watch</a></td></tr>
        <tr><td>85</td><td>Surah Al-Buruj</td><td><a href="https://youtu.be/UZvJebrIQfk?feature=shared">Watch</a></td></tr>
        <tr><td>86</td><td>Surah At-Tariq</td><td><a href="https://youtu.be/LLXn-kE-598?feature=shared">Watch</a></td></tr>
        <tr><td>87</td><td>Surah Al-A’la</td><td><a href="https://youtu.be/67gs-vCBaYI?feature=shared">Watch</a></td></tr>
        <tr><td>88</td><td>Surah Al-Ghashiyah</td><td><a href="https://youtu.be/vfoom6l6L4w?feature=shared">Watch</a></td></tr>
        <tr><td>89</td><td>Surah Al-Fajr</td><td><a href="https://youtu.be/72XHGhLre_8?feature=shared">Watch</a></td></tr>
        <tr><td>90</td><td>Surah Al-Balad</td><td><a href="https://youtu.be/PlXaz9onniw?feature=shared">Watch</a></td></tr>
        <tr><td>91</td><td>Surah Ash-Shams</td><td><a href="https://youtu.be/fIYk6ioKPDM?feature=shared">Watch</a></td></tr>
        <tr><td>92</td><td>Surah Al-Lail</td><td><a href="https://youtu.be/_pMLBImgEvk?feature=shared">Watch</a></td></tr>
        <tr><td>93</td><td>Surah Ad-Duha</td><td><a href="https://youtu.be/r3wCitqDxF8?feature=shared">Watch</a></td></tr>
        <tr><td>94</td><td>Surah Ash-Sharh</td><td><a href="https://youtu.be/59snlUGtDmQ?feature=shared">Watch</a></td></tr>
        <tr><td>95</td><td>Surah At-Tin</td><td><a href="https://youtu.be/tHy1k14w9xk?feature=shared">Watch</a></td></tr>
        <tr><td>96</td><td>Surah Al-Alaq</td><td><a href="https://youtu.be/JZ_yfEoJf6M?feature=shared">Watch</a></td></tr>
        <tr><td>97</td><td>Surah Al-Qadr</td><td><a href="https://youtu.be/VLDvWxqUK7A?feature=shared">Watch</a></td></tr>
        <tr><td>98</td><td>Surah Al-Bayyina</td><td><a href="https://youtu.be/U-1bn6IisXg?feature=shared">Watch</a></td></tr>
        <tr><td>99</td><td>Surah Az-Zalzalah</td><td><a href="https://youtu.be/AwCQfhh_Sh8?feature=shared">Watch</a></td></tr>
        <tr><td>100</td><td>Surah Al-Adiyat</td><td><a href="https://youtu.be/YaOZS4ZoRY8?feature=shared">Watch</a></td></tr>
        <tr><td>101</td><td>Surah Al-Qari’ah</td><td><a href="https://youtu.be/gmdTyUr4DzA?feature=shared">Watch</a></td></tr>
        <tr><td>102</td><td>Surah At-Takathur</td><td><a href="https://youtu.be/mkOwo41gkp8?feature=shared">Watch</a></td></tr>
        <tr><td>103</td><td>Surah Al-Asr</td><td><a href="https://youtu.be/-I2RkWeQvuo?feature=shared">Watch</a></td></tr>
        <tr><td>104</td><td>Surah Al-Humazah</td><td><a href="https://youtu.be/rnST2MaCjrY?feature=shared">Watch</a></td></tr>
        <tr><td>105</td><td>Surah Al-Fil</td><td><a href="https://youtu.be/4C3FZjkIKKo?feature=shared">Watch</a></td></tr>
        <tr><td>106</td><td>Surah Quraish</td><td><a href="https://youtu.be/wktEC7Jp5CU?feature=shared">Watch</a></td></tr>
        <tr><td>107</td><td>Surah Al-Ma’un</td><td><a href="https://youtu.be/l8VF5p4oPDE?feature=shared">Watch</a></td></tr>
        <tr><td>108</td><td>Surah Al-Kawthar</td><td><a href="https://youtu.be/gguAmbBNhJQ?feature=shared">Watch</a></td></tr>
        <tr><td>109</td><td>Surah Al-Kafirun</td><td><a href="https://youtu.be/4CvUCt_7t9Y?feature=shared">Watch</a></td></tr>
        <tr><td>110</td><td>Surah An-Nasr</td><td><a href="https://youtu.be/MVE1Mozt23w?feature=shared">Watch</a></td></tr>
        <tr><td>111</td><td>Surah Al-Masad</td><td><a href="https://youtu.be/M3dBqRX32fI?feature=shared">Watch</a></td></tr>
        <tr><td>112</td><td>Surah Al-Ikhlas</td><td><a href="https://youtu.be/fyub76Z1YW8?feature=shared">Watch</a></td></tr>
        <tr><td>113</td><td>Surah Al-Falaq</td><td><a href="https://youtu.be/MaOepE0iVP0?feature=shared">Watch</a></td></tr>
        <tr><td>114</td><td>Surah An-Nas</td><td><a href="https://youtu.be/5UTXy190B-I?feature=shared">Watch</a></td></tr>
    </table>
""", unsafe_allow_html=True)



st.markdown('</div>', unsafe_allow_html=True)


