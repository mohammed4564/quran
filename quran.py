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

st.write("View & Read the Quran PDF")
webpage_urly = 'https://www.islamicnet.com/quran.php'
st.markdown(f'<iframe src="{webpage_urly}" width="800" height="600"></iframe>', unsafe_allow_html=True)

st.write("Quran MP3 Files")
webpage_url = 'https://quranicaudio.com/'
st.markdown(f'<iframe src="{webpage_url}" width="800" height="600"></iframe>', unsafe_allow_html=True)


st.write('Full Quran Recitation Videos')
st.write("[Surah No 1 : Surah Fathihah - By Sheikh Abdur Rahman As Sudais](https://youtu.be/u1nqafqyqTA?feature=shared)")
st.write("[Surah No 2 : Surah Al Baqrah - By Sheikh Abdur Rahman As Sudais](https://youtu.be/nibOG3vRGpU?feature=shared)")
st.write("[Surah No 3 : Surah Al Imran - By Sheikh Abdur Rahman As Sudais ](https://youtu.be/tf26W_1mdFg?feature=shared)")
st.write("[Surah No 4 : Surah An Nisa - By Sheikh Abdur Rahman As Sudais](https://youtu.be/G0NqWjlXlQE?feature=shared)")
st.write("[Surah No 5 : Surah Al Maaidah - By Sheikh Abdur Rahman As Sudais](https://youtu.be/EFgAy0OP7CM?feature=shared)")
st.write("[Surah No 6 : Surah Al An Aam - By Sheikh Abdur Rahman As Sudais](https://youtu.be/RKXrMg14DaU?feature=shared)")
st.write("[Surah No 7 : Surah Al Araaf - By Sheikh Abdur Rahman As Sudais](https://youtu.be/GxDjbom4nIg?feature=shared)")
st.write("[Surah No 8 : Surah Al Anfal - By Sheikh Abdur Rahman As Sudais](https://youtu.be/tIoCEBUmrQU?feature=shared)")
st.write("[Surah No 9 : Surah At Thubah - By Sheikh Abdur Rahman As Sudais](https://youtu.be/4RoQ_FkdH_c?feature=shared)")
st.write("[Surah No 10 : Surah Yunus - By Sheikh Abdur Rahman As Sudais](https://youtu.be/YkG3XTG1pJM?feature=shared)")
st.write("[Surah No 11 : Surah Hud - By Sheikh Abdur Rahman As Sudais](https://youtu.be/EIFJ43WBuVo?feature=shared)")
st.write("[Surah No 12 : Surah Yusuf - By Sheikh Abdur Rahman As Sudais](https://youtu.be/URVroBsLsl4?feature=shared)")
st.write("[Surah No 13 : Surah Ar Raad - By Sheikh Abdur Rahman As Sudais](https://youtu.be/v7zVkvzh4S8?feature=shared)")
st.write("[Surah No 14 : Surah Ibrahim - By Sheikh Abdur Rahman As Sudais](https://youtu.be/-0A1Uy_3BqE?feature=shared)")
st.write("[Surah No 15 : Surah Al Hijr - By Sheikh Abdur Rahman As Sudais](https://youtu.be/WslQRNymzYw?feature=shared)")
st.write("[Surah No 16 : Surah An Nahl - By Sheikh Abdur Rahman As Sudais](https://youtu.be/QHjmot_zB3M?feature=shared)")
st.write("[Surah No 17 : Surah Israh - By Sheikh Abdur Rahman As Sudais](https://youtu.be/xnc9HL6o5yQ?feature=shared)")
st.write("[Surah No 18 : Surah Al Kahf- By Sheikh Abdur Rahman As Sudais](https://youtu.be/znuTS6Q96Vs?feature=shared)")
st.write("[Surah No 19 : Surah Maryam - By Sheikh Abdur Rahman As Sudais](https://youtu.be/JaeLTXaOmiU?feature=shared)")
st.write("[Surah No 20 : Surah Taha - By Sheikh Abdur Rahman As Sudais](https://youtu.be/P99qEmtNSqo?feature=shared)")
st.write("[Surah No 21 : Surah Al Anbiya - By Sheikh Abdur Rahman As Sudais](https://youtu.be/v_DfkRPS-Ak?feature=shared)")
st.write("[Surah No 22: Surah Al Hajj- By Sheikh Abdur Rahman As Sudais](https://youtu.be/e4a3p8TgUw0?feature=shared)")
st.write("[Surah No 23 : Surah Al Muminun- By Sheikh Abdur Rahman As Sudais](https://youtu.be/l7k51vBeLD8?feature=shared)")
st.write("[Surah No 24: Surah An Nur - By Sheikh Abdur Rahman As Sudais](https://youtu.be/ezWh_uABBzQ?feature=shared)")
st.write("[Surah No 25 : Surah Al Furqan- By Sheikh Abdur Rahman As Sudais](https://youtu.be/btl5ytL8_Fk?feature=shared)")
st.write("[Surah No 26 : Surah Ash Shuara - By Sheikh Abdur Rahman As Sudais](https://youtu.be/SrtlaNMRRw4?feature=shared)")
st.write("[Surah No 27 : Surah An Naml - By Sheikh Abdur Rahman As Sudais](https://youtu.be/q8vS7jzIph4?feature=shared)")
st.write("[Surah No 28: Surah Al Qasas- By Sheikh Abdur Rahman As Sudaisc](https://youtu.be/zUEzIrYc2eI?feature=shared)")
st.write("[Surah No 29: Surah Al Ankabut - By Sheikh Abdur Rahman As Sudais](https://youtu.be/mMYP6kuTSx0?feature=shared)")
st.write("[Surah No 30 : Surah Ar Rum- By Sheikh Abdur Rahman As Sudais](https://youtu.be/22bWGmjtE9Y?feature=shared)")
st.write("[Surah No 31 : Surah Luqman - By Sheikh Abdur Rahman As Sudais](https://youtu.be/BSvQ9LQ78Cs?feature=shared)")
st.write("[Surah No 32 : Surah As Sajdah - By Sheikh Abdur Rahman As Sudais](https://youtu.be/CiQIHvku7nU?feature=shared)")
st.write("[Surah No 33 : Surah Al Ahzab - By Sheikh Abdur Rahman As Sudais](https://youtu.be/u8S2zJpprZI?feature=shared)")
st.write("[Surah No 34 : Surah Saba - By Sheikh Abdur Rahman As Sudais](https://youtu.be/lTTAFbgmJe0?feature=shared)")
st.write("[Surah No 35 : Surah Fathir - By Sheikh Abdur Rahman As Sudais](https://youtu.be/389WDzOLksA?feature=shared)")
st.write("[Surah No 36 : Surah Yaseen - By Sheikh Abdur Rahman As Sudais](https://youtu.be/emousr_FIHI?feature=shared)")
st.write("[Surah No 37: Surah As Saffat - By Sheikh Abdur Rahman As Sudais](https://youtu.be/WiRy0sl7JZ8?feature=shared)")
st.write("[Surah No 38 : Surah Saad - By Sheikh Abdur Rahman As Sudais](https://youtu.be/PBFKqO56c-4?feature=shared)")
st.write("[Surah No 39 : Surah Az Zumar - By Sheikh Abdur Rahman As Sudais](https://youtu.be/1yGVVFet_BI?feature=shared)")
st.write("[Surah No 40 : Surah Ghafir - By Sheikh Abdur Rahman As Sudais](https://youtu.be/SFLaFHI7Kww?feature=shared)")
st.write("[Surah No 41 : Surah Fussilat - By Sheikh Abdur Rahman As Sudais](https://youtu.be/wuji4xmdOEw?feature=shared)")
st.write("[Surah No 42 : Surah Ash Shurah - By Sheikh Abdur Rahman As Sudais](https://youtu.be/cmIwH5ar_7M?feature=shared)")
st.write("[Surah No 43 : Surah Az Zukhruf - By Sheikh Abdur Rahman As Sudais](https://youtu.be/4iGCJI4xZrg?feature=shared)")
st.write("[Surah No 44 : Surah Ad Dukhan - By Sheikh Abdur Rahman As Sudais](https://youtu.be/uSXcJmiSsTo?feature=shared)")
st.write("[Surah No 45 : Surah Jathiyah - By Sheikh Abdur Rahman As Sudais](https://youtu.be/2AkyfRIR5lw?feature=shared)")
st.write("[Surah No 46 : Surah Ahqaaf - By Sheikh Abdur Rahman As Sudais](https://youtu.be/RkP5RDTfhEo?feature=shared)")
st.write("[Surah No 47 : Surah Muhammad - By Sheikh Abdur Rahman As Sudais](https://youtu.be/F7gqhhxkUJ8?feature=shared)")
st.write("[Surah No 48: Surah Al Fath - By Sheikh Abdur Rahman As Sudais](https://youtu.be/wr8TDXjA8kw?feature=shared)")
st.write("[Surah No 49 : Surah Al Hujurat - By Sheikh Abdur Rahman As Sudais](https://youtu.be/Hkf4UCVC_yU?feature=shared)")
st.write("[Surah No :50 - Surah Qaaf- By Sheikh Abdur Rahman As Sudais](https://youtu.be/oxMD-BX3IXE?feature=shared)")
st.write("[Surah No 51 : Surah Dhariyath - By Sheikh Abdur Rahman As Sudais](https://youtu.be/6TexBrmYc70?feature=shared)")
st.write("[Surah No 52 : Surah Ath Thoor - By Sheikh Abdur Rahman As Sudais](https://youtu.be/ykjOEXwxhOI?feature=shared)")
st.write("[Surah No 53 : Surah Najm - By Sheikh Abdur Rahman As Sudais](https://youtu.be/H_vEYQ4wuDQ?feature=shared)")
st.write("[Surah No 54 : Surah Qamar - By Sheikh Abdur Rahman As Sudais](https://youtu.be/BbrtnTvKePo?feature=shared)")
st.write("[Surah No 55 : Surah Ar Rahmaan - By Sheikh Abdur Rahman As Sudais](https://youtu.be/muhKlnac-i0?feature=shared)")
st.write("[Surah No 56 : Surah Waqiah - By Sheikh Abdur Rahman As Sudais](https://youtu.be/aubS8TecslU?feature=shared)")
st.write("[Surah No 57 : Surah Hadeed - By Sheikh Abdur Rahman As Sudais](https://youtu.be/bAy8IZsfhm0?feature=shared)")
st.write("[Surah No 58 : Surah Mujadhala - By Sheikh Abdur Rahman As Sudais](https://youtu.be/BM_r_xgjj_8?feature=shared)")
st.write("[Surah No 59 : Surah Hashr - By Sheikh Abdur Rahman As Sudais](https://youtu.be/Rdhva9_0p4o?feature=shared)")
st.write("[Surah No 60 : Surah Mumtahanah - By Sheikh Abdur Rahman As Sudais](https://youtu.be/DdtiCjO2N-g?feature=shared)")
st.write("[Surah No 61 : Surah As Saf - By Sheikh Abdur Rahman As Sudais](https://youtu.be/shU3cHdOSkg?feature=shared)")
st.write("[Surah No 62 : Surah Jum Ah - By Sheikh Abdur Rahman As Sudais](https://youtu.be/cW7XmILB4II?feature=shared)")
st.write("[Surah No 63 : Surah Munafiqoon - By Sheikh Abdur Rahman As Sudais](https://youtu.be/oagkbDU8m5I?feature=shared)")
st.write("[Surah No 64 : Surah Tahaabun - By Sheikh Abdur Rahman As Sudais](https://youtu.be/LlUYSVq4zlA?feature=shared)")
st.write("[Surah No 65 : Surah Thalaaq - By Sheikh Abdur Rahman As Sudais](https://youtu.be/xOoC0SV27_4?feature=shared)")
st.write("[Surah No 66 : Surah Thahreem - By Sheikh Abdur Rahman As Sudais](https://youtu.be/Bo4vM6_HltM?feature=shared)")
st.write("[Surah No 67 : Surah Mulk - By Sheikh Abdur Rahman As Sudais](https://youtu.be/q6EWyyplP9o?feature=shared)")
st.write("[Surah No 68 : Surah Qalam - By Sheikh Abdur Rahman As Sudais](https://youtu.be/QCM3pcnlhPo?feature=shared)")
st.write("[Surah No 69 : Surah Haaqqa - By Sheikh Abdur Rahman As Sudais](https://youtu.be/62RIS_q4FZo?feature=shared)")
st.write("[Surah No 70 : Surah Maarij - By Sheikh Abdur Rahman As Sudais](https://youtu.be/l7_5T6_WQ7s?feature=shared)")
st.write("[Surah No : 71 - Sharh Nooh - By Sheikh Abdur Rahman As Sudais](https://youtu.be/GRJoa7xY1Tc?feature=shared)")
st.write("[Surah No : 72 - Sharh Al Jinn - By Sheikh Abdur Rahman As Sudais](https://youtu.be/Sfkyz_gGkXw?feature=shared)")
st.write("[Surah No : 73 - Sharh Muzammil - By Sheikh Abdur Rahman As Sudais](https://youtu.be/b5Tq2g6ynq4?feature=shared)")
st.write("[Surah No : 74 - Sharh Muddaththir - By Sheikh Abdur Rahman As Sudais](https://youtu.be/E_ZaCciNn54?feature=shared)")
st.write("[Surah No : 75 - Sharh Qiyama - By Sheikh Abdur Rahman As Sudais](https://youtu.be/gGW5LuQghGk?feature=shared)")
st.write("[Surah No : 76 - Sharh Ath Thahr- By Sheikh Abdur Rahman As Sudais](https://youtu.be/TLEuyKG2buM?feature=shared)")
st.write("[Surah No : 77 - Sharh Mursalat - By Sheikh Abdur Rahman As Sudais](https://youtu.be/MDHz8PpAiyA?feature=sharedv)")
st.write("[Surah No : 78 - Sharh Naba - By Sheikh Abdur Rahman As Sudais](https://youtu.be/M_jrwXBOl1M?feature=shared)")
st.write("[Surah No : 79 - Sharh Naziath - By Sheikh Abdur Rahman As Sudais](https://youtu.be/XudZNuxm5zk?feature=shared)")
st.write("[Surah No : 80 - Sharh Abasa - By Sheikh Abdur Rahman As Sudais](https://youtu.be/9a5-TxG5GRs?feature=shared)")
st.write("[Surah No 81 : Surah At Takwir - By Sheikh Abdur Rahman As Sudais](https://youtu.be/gNQd6FQLsvQ?feature=shared)")
st.write("[Surah No 82 : Surah Infitar - By Sheikh Abdur Rahman As Sudais](https://youtu.be/8LosxlqhaTk?feature=shared)")
st.write("[Surah No 83 : Surah Al Mutaffifin - By Sheikh Abdur Rahman As Sudais](https://youtu.be/VFAxRV9a-w0?feature=shared)")
st.write("[Surah No : 84 - Sharh Inshiqaaq - By Sheikh Abdur Rahman As Sudais](https://youtu.be/p_in_GR-neY?feature=shared)")
st.write("[Surah No : 85 - Sharh Al Burooj - By Sheikh Abdur Rahman As Sudais](https://youtu.be/gwKC9W18TrA?feature=shared)")
st.write("[Surah No : 86 - Sharh Ath Thariq - By Sheikh Abdur Rahman As Sudais](https://youtu.be/wEOZsvLyS74?feature=shared)")
st.write("[Surah No : 87 - Ala - By Sheikh Abdur Rahman As Sudais](https://youtu.be/pHUWDzMRZW8?feature=shared)")
st.write("[Surah No : 88 - Ghashiyah - By Sheikh Abdur Rahman As Sudais](https://youtu.be/mfuCi8alrb8?feature=shared)")
st.write("[Surah No : 89 - Fajr - By Sheikh Abdur Rahman As Sudais](https://youtu.be/eKZ38VYtHuI?feature=shared)")
st.write("[Surah No : 90 - Sharh Al Balad - By Sheikh Abdur Rahman As Sudais](https://youtu.be/FsdfNGIBIYs?feature=shared)")
st.write("[Surah No : 91 - Shams - By Sheikh Abdur Rahman As Sudais](https://youtu.be/bGqmBo9rcs4?feature=shared)")
st.write("[Surah No : 92 - Sharh Al Lail - By Sheikh Abdur Rahman As Sudais](https://youtu.be/AH1mYJTLOwo?feature=shared)")
st.write("[Surah No : 93 - Dhuha - By Sheikh Abdur Rahman As Sudais](https://youtu.be/cqMI5RCBivg?feature=shared)")
st.write("[Surah No : 94 - Sharh - By Sheikh Abdur Rahman As Sudais](https://youtu.be/ZMpZhlGFfME?feature=shared)")
st.write("[Surah No : 95 - At Thin- By Sheikh Abdur Rahman As Sudais](https://youtu.be/4tgptyV-CQA?feature=shared)")
st.write("[Surah No : 96 - Alaq - By Sheikh Abdur Rahman As Sudais](https://youtu.be/ElrBVCDj9mk?feature=shared)")
st.write("[Surah No : 97- Qadr - By Sheikh Abdur Rahman As Sudais](https://youtu.be/0fNYbCjcJ9o?feature=shared)")
st.write("[Surah No : 98 - Bayyina - By Sheikh Abdur Rahman As Sudais](https://youtu.be/rlXOFhcbE6M?feature=shared)")
st.write("[Surah No : 99 - Zalzalah - By Sheikh Abdur Rahman As Sudais](https://youtu.be/nOaLcB4KliM?feature=shared)")
st.write("[Surah No 100 : Surah Al Adiyat - By Sheikh Abdur Rahman As Sudais](https://youtu.be/lIJwwgBt0xQ?feature=shared)")
st.write("[Surah No :101 - Surah Qaria - By Sheikh Abdur Rahman As Sudais](https://youtu.be/0VauU7RJ0J8?feature=shared)")
st.write("[Surah No :102 - SurahTakathur - By Sheikh Abdur Rahman As Sudais](https://youtu.be/tvFyrElP75I?feature=shared)")
st.write("[Surah No : 103 - Al Asr - By Sheikh Abdur Rahman As Sudais](https://youtu.be/Jq99D7AV8VU?feature=shared)")
st.write("[Surah No :104 - Surah Humazah - By Sheikh Abdur Rahman As Sudais](https://youtu.be/ycDTGWBNVGs?feature=shared)")
st.write("[Surah No :105 - Surah Fil - By Sheikh Abdur Rahman As Sudais](https://youtu.be/lrzYf_DEYPI?feature=shared)")
st.write("[Surah No :106 - Surah Quraish - By Sheikh Abdur Rahman As Sudais](https://youtu.be/2f5cwqnCT8Q?feature=shared)")
st.write("[Surah No :107 - Surah Maaun - By Sheikh Abdur Rahman As Sudais](https://youtu.be/T3pEGIbC2Bc?feature=shared)")
st.write("[Surah No :108 - Surah Kauthar - By Sheikh Abdur Rahman As Sudais](https://youtu.be/FqHigXI9Ucw?feature=shared)")
st.write("[Surah No :109 - Surah Kafiroon - By Sheikh Abdur Rahman As Sudais](https://youtu.be/D1g4BLIjTes?feature=shared)")
st.write("[Surah No :110 - Surah Nasr - By Sheikh Abdur Rahman As Sudais](https://youtu.be/VItrsgKSj6Q?feature=shared)")
st.write("[Surah No :111 - Surah Masad - By Sheikh Abdur Rahman As Sudais](https://youtu.be/Si5LoKGkxzE?feature=shared)")
st.write("[Surah No :112 - Surah Iqlas - By Sheikh Abdur Rahman As Sudais](https://youtu.be/dtnhtsbaFG8?feature=shared)")
st.write("[Surah No :113 - Surah Falak - By Sheikh Abdur Rahman As Sudais](https://youtu.be/gUtD5O5AmaQ?feature=shared)")
st.write("[Surah No :114 - Surah An Naas - By Sheikh Abdur Rahman As Sudais](https://youtu.be/ZIUSO7aAJPY?feature=shared)")

st.markdown('</div>', unsafe_allow_html=True)


