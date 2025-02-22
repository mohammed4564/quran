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

# Styling the text
# Add custom CSS to style the header text
# Add a beautiful custom-styled heading
st.markdown("""
    <p style="font-size: 36px; font-weight: bold; color: #2ecc71; text-align: center;">
        <span style="color: #8e44ad;">Sacred</span> Quran <span style="color: #f39c12;">MP3</span> Collection
    </p>
""", unsafe_allow_html=True)

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
        <tr><td>6</td><td>Surah Al-An’am</td><td><a href="https://youtu.be/RKXrMg14DaU?feature=shared">Watch</a></td></tr>
        <tr><td>7</td><td>Surah Al-A’raf</td><td><a href="https://youtu.be/GxDjbom4nIg?feature=shared">Watch</a></td></tr>
        <tr><td>8</td><td>Surah Al-Anfal</td><td><a href="https://youtu.be/tIoCEBUmrQU?feature=shared">Watch</a></td></tr>
        <tr><td>9</td><td>Surah At-Tawbah</td><td><a href="https://youtu.be/4RoQ_FkdH_c?feature=shared">Watch</a></td></tr>
        <tr><td>10</td><td>Surah Yunus</td><td><a href="https://youtu.be/YkG3XTG1pJM?feature=shared">Watch</a></td></tr>
        <tr><td>11</td><td>Surah Hud</td><td><a href="https://youtu.be/EIFJ43WBuVo?feature=shared">Watch</a></td></tr>
        <tr><td>12</td><td>Surah Yusuf</td><td><a href="https://youtu.be/URVroBsLsl4?feature=shared">Watch</a></td></tr>
        <tr><td>13</td><td>Surah Ar-Ra’d</td><td><a href="https://youtu.be/v7zVkvzh4S8?feature=shared">Watch</a></td></tr>
        <tr><td>14</td><td>Surah Ibrahim</td><td><a href="https://youtu.be/-0A1Uy_3BqE?feature=shared">Watch</a></td></tr>
        <tr><td>15</td><td>Surah Al-Hijr</td><td><a href="https://youtu.be/WslQRNymzYw?feature=shared">Watch</a></td></tr>
        <tr><td>16</td><td>Surah An-Nahl</td><td><a href="https://youtu.be/QHjmot_zB3M?feature=shared">Watch</a></td></tr>
        <tr><td>17</td><td>Surah Al-Isra</td><td><a href="https://youtu.be/xnc9HL6o5yQ?feature=shared">Watch</a></td></tr>
        <tr><td>18</td><td>Surah Al-Kahf</td><td><a href="https://youtu.be/znuTS6Q96Vs?feature=shared">Watch</a></td></tr>
        <tr><td>19</td><td>Surah Maryam</td><td><a href="https://youtu.be/JaeLTXaOmiU?feature=shared">Watch</a></td></tr>
        <tr><td>20</td><td>Surah Taha</td><td><a href="https://youtu.be/P99qEmtNSqo?feature=shared">Watch</a></td></tr>
        <tr><td>21</td><td>Surah Al-Anbiya</td><td><a href="https://youtu.be/v_DfkRPS-Ak?feature=shared">Watch</a></td></tr>
        <tr><td>22</td><td>Surah Al-Hajj</td><td><a href="https://youtu.be/e4a3p8TgUw0?feature=shared">Watch</a></td></tr>
        <tr><td>23</td><td>Surah Al-Mu’minun</td><td><a href="https://youtu.be/l7k51vBeLD8?feature=shared">Watch</a></td></tr>
        <tr><td>24</td><td>Surah An-Nur</td><td><a href="https://youtu.be/ezWh_uABBzQ?feature=shared">Watch</a></td></tr>
        <tr><td>25</td><td>Surah Al-Furqan</td><td><a href="https://youtu.be/btl5ytL8_Fk?feature=shared">Watch</a></td></tr>
        <tr><td>26</td><td>Surah Ash-Shu’ara</td><td><a href="https://youtu.be/SrtlaNMRRw4?feature=shared">Watch</a></td></tr>
        <tr><td>27</td><td>Surah An-Naml</td><td><a href="https://youtu.be/q8vS7jzIph4?feature=shared">Watch</a></td></tr>
        <tr><td>28</td><td>Surah Al-Qasas</td><td><a href="https://youtu.be/zUEzIrYc2eI?feature=shared">Watch</a></td></tr>
        <tr><td>29</td><td>Surah Al-Ankabut</td><td><a href="https://youtu.be/mMYP6kuTSx0?feature=shared">Watch</a></td></tr>
        <tr><td>30</td><td>Surah Ar-Rum</td><td><a href="https://youtu.be/22bWGmjtE9Y?feature=shared">Watch</a></td></tr>
        <tr><td>31</td><td>Surah Luqman</td><td><a href="https://youtu.be/BSvQ9LQ78Cs?feature=shared">Watch</a></td></tr>
        <tr><td>32</td><td>Surah As-Sajdah</td><td><a href="https://youtu.be/CiQIHvku7nU?feature=shared">Watch</a></td></tr>
        <tr><td>33</td><td>Surah Al-Ahzab</td><td><a href="https://youtu.be/u8S2zJpprZI?feature=shared">Watch</a></td></tr>
        <tr><td>34</td><td>Surah Saba</td><td><a href="https://youtu.be/lTTAFbgmJe0?feature=shared">Watch</a></td></tr>
        <tr><td>35</td><td>Surah Fatir</td><td><a href="https://youtu.be/389WDzOLksA?feature=shared">Watch</a></td></tr>
        <tr><td>36</td><td>Surah Yaseen</td><td><a href="https://youtu.be/emousr_FIHI?feature=shared">Watch</a></td></tr>
        <tr><td>37</td><td>Surah As-Saffat</td><td><a href="https://youtu.be/WiRy0slgXyk?feature=shared">Watch</a></td></tr>
        <tr><td>38</td><td>Surah Sad</td><td><a href="https://youtu.be/KyxRE7HJUL8?feature=shared">Watch</a></td></tr>
        <tr><td>39</td><td>Surah Az-Zumar</td><td><a href="https://youtu.be/5yZ7VpTR5WU?feature=shared">Watch</a></td></tr>
        <tr><td>40</td><td>Surah Ghafir</td><td><a href="https://youtu.be/X9Os8eP8khw?feature=shared">Watch</a></td></tr>
        <tr><td>41</td><td>Surah Fussilat</td><td><a href="https://youtu.be/N6yFJ2nsSTw?feature=shared">Watch</a></td></tr>
        <tr><td>42</td><td>Surah Ash-Shura</td><td><a href="https://youtu.be/3w2JJFdB2rk?feature=shared">Watch</a></td></tr>
        <tr><td>43</td><td>Surah Az-Zukhruf</td><td><a href="https://youtu.be/ZqbnkVmL5h8?feature=shared">Watch</a></td></tr>
        <tr><td>44</td><td>Surah Ad-Dukhan</td><td><a href="https://youtu.be/LyAogP_0W-4?feature=shared">Watch</a></td></tr>
        <tr><td>45</td><td>Surah Al-Jathiya</td><td><a href="https://youtu.be/mrEbbYtuvp8?feature=shared">Watch</a></td></tr>
        <tr><td>46</td><td>Surah Al-Ahqaf</td><td><a href="https://youtu.be/WnD9t6W3_MA?feature=shared">Watch</a></td></tr>
        <tr><td>47</td><td>Surah Muhammad</td><td><a href="https://youtu.be/D7u7Ac5tAm4?feature=shared">Watch</a></td></tr>
        <tr><td>48</td><td>Surah Al-Fath</td><td><a href="https://youtu.be/J1pZdtZzD7o?feature=shared">Watch</a></td></tr>
        <tr><td>49</td><td>Surah Al-Hujurat</td><td><a href="https://youtu.be/xChWcXEB8As?feature=shared">Watch</a></td></tr>
        <tr><td>50</td><td>Surah Qaf</td><td><a href="https://youtu.be/gKXJ5aGOHZc?feature=shared">Watch</a></td></tr>
        <tr><td>51</td><td>Surah Adh-Dhariyat</td><td><a href="https://youtu.be/Y9LgQ5OX4hQ?feature=shared">Watch</a></td></tr>
        <tr><td>52</td><td>Surah At-Tur</td><td><a href="https://youtu.be/vyHq1vX8Y2I?feature=shared">Watch</a></td></tr>
        <tr><td>53</td><td>Surah An-Najm</td><td><a href="https://youtu.be/j_XjjlsWxUo?feature=shared">Watch</a></td></tr>
        <tr><td>54</td><td>Surah Al-Qamar</td><td><a href="https://youtu.be/4UjtSrwTb0o?feature=shared">Watch</a></td></tr>
        <tr><td>55</td><td>Surah Ar-Rahman</td><td><a href="https://youtu.be/YzJ4BxCZtFA?feature=shared">Watch</a></td></tr>
        <tr><td>56</td><td>Surah Al-Waqi’ah</td><td><a href="https://youtu.be/V3kpcCHC53A?feature=shared">Watch</a></td></tr>
        <tr><td>57</td><td>Surah Al-Hadid</td><td><a href="https://youtu.be/NOG5V5Yfm6g?feature=shared">Watch</a></td></tr>
        <tr><td>58</td><td>Surah Al-Mujadila</td><td><a href="https://youtu.be/kRKM7S5Bss8?feature=shared">Watch</a></td></tr>
        <tr><td>59</td><td>Surah Al-Hashr</td><td><a href="https://youtu.be/fXJ57EnkGrI?feature=shared">Watch</a></td></tr>
        <tr><td>60</td><td>Surah Al-Mumtahina</td><td><a href="https://youtu.be/KCjq0h4uFh0?feature=shared">Watch</a></td></tr>
        <tr><td>61</td><td>Surah As-Saff</td><td><a href="https://youtu.be/JhvFf-NyIMI?feature=shared">Watch</a></td></tr>
        <tr><td>62</td><td>Surah Al-Jumu’a</td><td><a href="https://youtu.be/zpZZd7qdPC8?feature=shared">Watch</a></td></tr>
        <tr><td>63</td><td>Surah Al-Munafiqun</td><td><a href="https://youtu.be/Xw_WP-lhpAY?feature=shared">Watch</a></td></tr>
        <tr><td>64</td><td>Surah At-Taghabun</td><td><a href="https://youtu.be/f0g39cz0gg8?feature=shared">Watch</a></td></tr>
        <tr><td>65</td><td>Surah At-Talaq</td><td><a href="https://youtu.be/f8ld36ewwVo?feature=shared">Watch</a></td></tr>
        <tr><td>66</td><td>Surah At-Tahrim</td><td><a href="https://youtu.be/59X9yycA5FE?feature=shared">Watch</a></td></tr>
        <tr><td>67</td><td>Surah Al-Mulk</td><td><a href="https://youtu.be/YI7OGXOrW9I?feature=shared">Watch</a></td></tr>
        <tr><td>68</td><td>Surah Al-Qalam</td><td><a href="https://youtu.be/wIMEXhFwzCk?feature=shared">Watch</a></td></tr>
        <tr><td>69</td><td>Surah Al-Haqqah</td><td><a href="https://youtu.be/hsU3EzL7DK0?feature=shared">Watch</a></td></tr>
        <tr><td>70</td><td>Surah Al-Maarij</td><td><a href="https://youtu.be/B0quz_4q8IE?feature=shared">Watch</a></td></tr>
        <tr><td>71</td><td>Surah Nuh</td><td><a href="https://youtu.be/Zr_W6lswiy4?feature=shared">Watch</a></td></tr>
        <tr><td>72</td><td>Surah Al-Jinn</td><td><a href="https://youtu.be/U92_aYPXmwY?feature=shared">Watch</a></td></tr>
        <tr><td>73</td><td>Surah Al-Muzzammil</td><td><a href="https://youtu.be/Sjfa9rZ6P40?feature=shared">Watch</a></td></tr>
        <tr><td>74</td><td>Surah Al-Muddathir</td><td><a href="https://youtu.be/BHgAqvWOhzY?feature=shared">Watch</a></td></tr>
        <tr><td>75</td><td>Surah Al-Qiyamah</td><td><a href="https://youtu.be/n-TFqpkKrAs?feature=shared">Watch</a></td></tr>
        <tr><td>76</td><td>Surah Al-Insan</td><td><a href="https://youtu.be/gHRR02BDOTs?feature=shared">Watch</a></td></tr>
        <tr><td>77</td><td>Surah Al-Mursalat</td><td><a href="https://youtu.be/g9w-X_Oe0sM?feature=shared">Watch</a></td></tr>
        <tr><td>78</td><td>Surah An-Naba</td><td><a href="https://youtu.be/f8lkZ1glEdA?feature=shared">Watch</a></td></tr>
        <tr><td>79</td><td>Surah An-Nazi’at</td><td><a href="https://youtu.be/vT5MiRzLfoc?feature=shared">Watch</a></td></tr>
        <tr><td>80</td><td>Surah Abasa</td><td><a href="https://youtu.be/hJrp0FmjCfs?feature=shared">Watch</a></td></tr>
        <tr><td>81</td><td>Surah At-Takwir</td><td><a href="https://youtu.be/oTfohd5p4Ks?feature=shared">Watch</a></td></tr>
        <tr><td>82</td><td>Surah Al-Infitar</td><td><a href="https://youtu.be/2iiu3G3jBEI?feature=shared">Watch</a></td></tr>
        <tr><td>83</td><td>Surah Al-Mutaffifin</td><td><a href="https://youtu.be/9kJbFu2Ylrk?feature=shared">Watch</a></td></tr>
        <tr><td>84</td><td>Surah Al-Inshiqaq</td><td><a href="https://youtu.be/JtIqB17STmY?feature=shared">Watch</a></td></tr>
        <tr><td>85</td><td>Surah Al-Buruj</td><td><a href="https://youtu.be/JuUP6G7bQ2Q?feature=shared">Watch</a></td></tr>
        <tr><td>86</td><td>Surah At-Tariq</td><td><a href="https://youtu.be/gc4EKvwN_aA?feature=shared">Watch</a></td></tr>
        <tr><td>87</td><td>Surah Al-A’la</td><td><a href="https://youtu.be/SMVNN_wlQTQ?feature=shared">Watch</a></td></tr>
        <tr><td>88</td><td>Surah Al-Ghashiyah</td><td><a href="https://youtu.be/qX5b5fWnFuE?feature=shared">Watch</a></td></tr>
        <tr><td>89</td><td>Surah Al-Fajr</td><td><a href="https://youtu.be/mkdoLmlpOC8?feature=shared">Watch</a></td></tr>
        <tr><td>90</td><td>Surah Al-Balad</td><td><a href="https://youtu.be/cFuy-bOkdzQ?feature=shared">Watch</a></td></tr>
        <tr><td>91</td><td>Surah Ash-Shams</td><td><a href="https://youtu.be/4h2nlAkhtCA?feature=shared">Watch</a></td></tr>
        <tr><td>92</td><td>Surah Al-Lail</td><td><a href="https://youtu.be/Lj_wYo-ULjI?feature=shared">Watch</a></td></tr>
        <tr><td>93</td><td>Surah Ad-Duha</td><td><a href="https://youtu.be/lEKLOwvyyEs?feature=shared">Watch</a></td></tr>
        <tr><td>94</td><td>Surah Ash-Sharh</td><td><a href="https://youtu.be/Op34OUvl3mA?feature=shared">Watch</a></td></tr>
        <tr><td>95</td><td>Surah At-Tin</td><td><a href="https://youtu.be/v0pDDbDEeGA?feature=shared">Watch</a></td></tr>
        <tr><td>96</td><td>Surah Al-Alaq</td><td><a href="https://youtu.be/vGyGmDgM4L0?feature=shared">Watch</a></td></tr>
        <tr><td>97</td><td>Surah Al-Qadr</td><td><a href="https://youtu.be/dS1nkIqNhzk?feature=shared">Watch</a></td></tr>
        <tr><td>98</td><td>Surah Al-Bayyina</td><td><a href="https://youtu.be/5J8PbbdddaY?feature=shared">Watch</a></td></tr>
        <tr><td>99</td><td>Surah Az-Zalzalah</td><td><a href="https://youtu.be/d58AzM89Zrg?feature=shared">Watch</a></td></tr>
        <tr><td>100</td><td>Surah Al-Adiyat</td><td><a href="https://youtu.be/mzA0QyGS4D8?feature=shared">Watch</a></td></tr>
        <tr><td>101</td><td>Surah Al-Qari’ah</td><td><a href="https://youtu.be/L0aFeIbmOvc?feature=shared">Watch</a></td></tr>
        <tr><td>102</td><td>Surah At-Takathur</td><td><a href="https://youtu.be/hqXfmp7_P6A?feature=shared">Watch</a></td></tr>
        <tr><td>103</td><td>Surah Al-Asr</td><td><a href="https://youtu.be/RiZ0ccK1S60?feature=shared">Watch</a></td></tr>
        <tr><td>104</td><td>Surah Al-Humazah</td><td><a href="https://youtu.be/U9sBR_zAk6M?feature=shared">Watch</a></td></tr>
        <tr><td>105</td><td>Surah Al-Fil</td><td><a href="https://youtu.be/ahQgr7LgkHs?feature=shared">Watch</a></td></tr>
        <tr><td>106</td><td>Surah Quraish</td><td><a href="https://youtu.be/nqks2x18bfw?feature=shared">Watch</a></td></tr>
        <tr><td>107</td><td>Surah Al-Ma’un</td><td><a href="https://youtu.be/K4V1qjvq4Xs?feature=shared">Watch</a></td></tr>
        <tr><td>108</td><td>Surah Al-Kawthar</td><td><a href="https://youtu.be/e5yxkOEZ6Z4?feature=shared">Watch</a></td></tr>
        <tr><td>109</td><td>Surah Al-Kafirun</td><td><a href="https://youtu.be/QpVnlfV7-KM?feature=shared">Watch</a></td></tr>
        <tr><td>110</td><td>Surah An-Nasr</td><td><a href="https://youtu.be/C6Z1lL3QRY4?feature=shared">Watch</a></td></tr>
        <tr><td>111</td><td>Surah Al-Masad</td><td><a href="https://youtu.be/0KroBd0MbCI?feature=shared">Watch</a></td></tr>
        <tr><td>112</td><td>Surah Al-Ikhlas</td><td><a href="https://youtu.be/P6mfdFzYmK4?feature=shared">Watch</a></td></tr>
        <tr><td>113</td><td>Surah Al-Falaq</td><td><a href="https://youtu.be/qLlzAGtOltQ?feature=shared">Watch</a></td></tr>
        <tr><td>114</td><td>Surah An-Nas</td><td><a href="https://youtu.be/X5vR4paBKrE?feature=shared">Watch</a></td></tr>
    </table>
""", unsafe_allow_html=True)


import streamlit as st
import pandas as pd

# Adding custom CSS for styling the app
st.markdown("""
    <style>
        .title {
            color: #4CAF50;
            font-size: 36px;
            text-align: center;
            font-weight: bold;
            margin-bottom: 30px;
        }
        .table th, .table td {
            padding: 12px;
            text-align: left;
            border: 1px solid #ddd;
            font-size: 14px;
        }
        .table th {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            font-size: 16px;
        }
        .table tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .table tr:nth-child(odd) {
            background-color: #e9f7ef;
        }
        .table tr:hover {
            background-color: #ddd;
        }
        .download-btn {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }
        .download-btn:hover {
            background-color: #45a049;
        }
        .para-name {
            color: #3e8e41;
            font-weight: bold;
        }
        .pdf-icon {
            font-size: 20px;
            color: #4CAF50;
        }
        .blue-text {
            color: #2980b9;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Adding the custom heading using HTML
st.markdown("""
    <p style="font-size: 24px; font-weight: bold; color: #e74c3c; text-align: center;">
        Quran Paras <span style="color: #2980b9;">PDF Download</span>
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

# Displaying the table with titles in blue
st.markdown("""
    <table class="table">
        <thead>
            <tr>
                <th class="blue-text">Sl.No</th>
                <th class="blue-text">Para Name</th>
                <th class="blue-text">Download PDF</th>
            </tr>
        </thead>
        <tbody>
""", unsafe_allow_html=True)

# Iterating over the list to display the Paras in the table
for i, para in enumerate(pdf_files, start=1):
    st.markdown(f"""
        <tr>
            <td>{i}</td>
            <td>{para["name"]} ({para["arabic_name"]})</td>
            <td><a href="{github_repo_url}{para['file']}" target="_blank" class="download-btn">
                    <i class="pdf-icon">📄</i> Download PDF</a></td>
        </tr>
    """, unsafe_allow_html=True)

# Closing the table
st.markdown("</tbody></table>", unsafe_allow_html=True)


st.markdown('</div>', unsafe_allow_html=True)


