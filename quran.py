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
st.write("""
    <table>
        <tr><th>Surah Number</th><th>Surah Name</th><th>Link</th></tr>
        <tr><td>1</td><td>Surah Fathihah</td><td><a href="https://youtu.be/u1nqafqyqTA?feature=shared">Watch</a></td></tr>
        <tr><td>2</td><td>Surah Al Baqrah</td><td><a href="https://youtu.be/nibOG3vRGpU?feature=shared">Watch</a></td></tr>
        <tr><td>3</td><td>Surah Al Imran</td><td><a href="https://youtu.be/tf26W_1mdFg?feature=shared">Watch</a></td></tr>
        <tr><td>4</td><td>Surah An Nisa</td><td><a href="https://youtu.be/G0NqWjlXlQE?feature=shared">Watch</a></td></tr>
        <tr><td>5</td><td>Surah Al Maaidah</td><td><a href="https://youtu.be/EFgAy0OP7CM?feature=shared">Watch</a></td></tr>
        <tr><td>6</td><td>Surah Al An Aam</td><td><a href="https://youtu.be/RKXrMg14DaU?feature=shared">Watch</a></td></tr>
        <tr><td>7</td><td>Surah Al Araaf</td><td><a href="https://youtu.be/GxDjbom4nIg?feature=shared">Watch</a></td></tr>
        <tr><td>8</td><td>Surah Al Anfal</td><td><a href="https://youtu.be/tIoCEBUmrQU?feature=shared">Watch</a></td></tr>
        <tr><td>9</td><td>Surah At Thubah</td><td><a href="https://youtu.be/4RoQ_FkdH_c?feature=shared">Watch</a></td></tr>
        <tr><td>10</td><td>Surah Yunus</td><td><a href="https://youtu.be/YkG3XTG1pJM?feature=shared">Watch</a></td></tr>
        <tr><td>11</td><td>Surah Hud</td><td><a href="https://youtu.be/EIFJ43WBuVo?feature=shared">Watch</a></td></tr>
        <tr><td>12</td><td>Surah Yusuf</td><td><a href="https://youtu.be/URVroBsLsl4?feature=shared">Watch</a></td></tr>
        <tr><td>13</td><td>Surah Ar Raad</td><td><a href="https://youtu.be/v7zVkvzh4S8?feature=shared">Watch</a></td></tr>
        <tr><td>14</td><td>Surah Ibrahim</td><td><a href="https://youtu.be/-0A1Uy_3BqE?feature=shared">Watch</a></td></tr>
        <tr><td>15</td><td>Surah Al Hijr</td><td><a href="https://youtu.be/WslQRNymzYw?feature=shared">Watch</a></td></tr>
        <tr><td>16</td><td>Surah An Nahl</td><td><a href="https://youtu.be/QHjmot_zB3M?feature=shared">Watch</a></td></tr>
        <tr><td>17</td><td>Surah Israh</td><td><a href="https://youtu.be/xnc9HL6o5yQ?feature=shared">Watch</a></td></tr>
        <tr><td>18</td><td>Surah Al Kahf</td><td><a href="https://youtu.be/znuTS6Q96Vs?feature=shared">Watch</a></td></tr>
        <tr><td>19</td><td>Surah Maryam</td><td><a href="https://youtu.be/JaeLTXaOmiU?feature=shared">Watch</a></td></tr>
        <tr><td>20</td><td>Surah Taha</td><td><a href="https://youtu.be/P99qEmtNSqo?feature=shared">Watch</a></td></tr>
        <tr><td>21</td><td>Surah Al Anbiya</td><td><a href="https://youtu.be/v_DfkRPS-Ak?feature=shared">Watch</a></td></tr>
        <tr><td>22</td><td>Surah Al Hajj</td><td><a href="https://youtu.be/e4a3p8TgUw0?feature=shared">Watch</a></td></tr>
        <tr><td>23</td><td>Surah Al Muminun</td><td><a href="https://youtu.be/l7k51vBeLD8?feature=shared">Watch</a></td></tr>
        <tr><td>24</td><td>Surah An Nur</td><td><a href="https://youtu.be/ezWh_uABBzQ?feature=shared">Watch</a></td></tr>
        <tr><td>25</td><td>Surah Al Furqan</td><td><a href="https://youtu.be/btl5ytL8_Fk?feature=shared">Watch</a></td></tr>
        <tr><td>26</td><td>Surah Ash Shuara</td><td><a href="https://youtu.be/SrtlaNMRRw4?feature=shared">Watch</a></td></tr>
        <tr><td>27</td><td>Surah An Naml</td><td><a href="https://youtu.be/q8vS7jzIph4?feature=shared">Watch</a></td></tr>
        <tr><td>28</td><td>Surah Al Qasas</td><td><a href="https://youtu.be/zUEzIrYc2eI?feature=shared">Watch</a></td></tr>
        <tr><td>29</td><td>Surah Al Ankabut</td><td><a href="https://youtu.be/mMYP6kuTSx0?feature=shared">Watch</a></td></tr>
        <tr><td>30</td><td>Surah Ar Rum</td><td><a href="https://youtu.be/22bWGmjtE9Y?feature=shared">Watch</a></td></tr>
        <tr><td>31</td><td>Surah Luqman</td><td><a href="https://youtu.be/BSvQ9LQ78Cs?feature=shared">Watch</a></td></tr>
        <tr><td>32</td><td>Surah As Sajdah</td><td><a href="https://youtu.be/CiQIHvku7nU?feature=shared">Watch</a></td></tr>
        <tr><td>33</td><td>Surah Al Ahzab</td><td><a href="https://youtu.be/u8S2zJpprZI?feature=shared">Watch</a></td></tr>
        <tr><td>34</td><td>Surah Saba</td><td><a href="https://youtu.be/lTTAFbgmJe0?feature=shared">Watch</a></td></tr>
        <tr><td>35</td><td>Surah Fathir</td><td><a href="https://youtu.be/389WDzOLksA?feature=shared">Watch</a></td></tr>
        <tr><td>36</td><td>Surah Yaseen</td><td><a href="https://youtu.be/emousr_FIHI?feature=shared">Watch</a></td></tr>
        <tr><td>37</td><td>Surah As Saffat</td><td><a href="https://youtu.be/WiRy0sl7JZ8?feature=shared">Watch</a></td></tr>
        <tr><td>38</td><td>Surah Saad</td><td><a href="https://youtu.be/PBFKqO56c-4?feature=shared">Watch</a></td></tr>
        <tr><td>39</td><td>Surah Az Zumar</td><td><a href="https://youtu.be/1yGVVFet_BI?feature=shared">Watch</a></td></tr>
        <tr><td>40</td><td>Surah Ghafir</td><td><a href="https://youtu.be/WqPMw7au_hA?feature=shared">Watch</a></td></tr>
        <tr><td>41</td><td>Surah Fussilat</td><td><a href="https://youtu.be/8Jk7U3_w_g8?feature=shared">Watch</a></td></tr>
        <tr><td>42</td><td>Surah Ash Shura</td><td><a href="https://youtu.be/VItjxwR6qnY?feature=shared">Watch</a></td></tr>
        <tr><td>43</td><td>Surah Az Zukhruf</td><td><a href="https://youtu.be/3z8gJg7bAyY?feature=shared">Watch</a></td></tr>
        <tr><td>44</td><td>Surah Ad Dukhan</td><td><a href="https://youtu.be/TwCpfnQYr5o?feature=shared">Watch</a></td></tr>
        <tr><td>45</td><td>Surah Al Jathiya</td><td><a href="https://youtu.be/-h0onW_Nt3A?feature=shared">Watch</a></td></tr>
        <tr><td>46</td><td>Surah Al Ahqaf</td><td><a href="https://youtu.be/mqOIb3OfH6g?feature=shared">Watch</a></td></tr>
        <tr><td>47</td><td>Surah Muhammad</td><td><a href="https://youtu.be/yEq7qFfLRpI?feature=shared">Watch</a></td></tr>
        <tr><td>48</td><td>Surah Al Fath</td><td><a href="https://youtu.be/wK6Ffa7bZX0?feature=shared">Watch</a></td></tr>
        <tr><td>49</td><td>Surah Al Hujurat</td><td><a href="https://youtu.be/R9se6pvo0OQ?feature=shared">Watch</a></td></tr>
        <tr><td>50</td><td>Surah Qaf</td><td><a href="https://youtu.be/nntoQZrnL0s?feature=shared">Watch</a></td></tr>
        <tr><td>51</td><td>Surah Adh Dhariyat</td><td><a href="https://youtu.be/LYp-bnyhLh4?feature=shared">Watch</a></td></tr>
        <tr><td>52</td><td>Surah At Tur</td><td><a href="https://youtu.be/ZAHNlp6OBj8?feature=shared">Watch</a></td></tr>
        <tr><td>53</td><td>Surah An Najm</td><td><a href="https://youtu.be/9z3yO0g4E44?feature=shared">Watch</a></td></tr>
        <tr><td>54</td><td>Surah Al Qamar</td><td><a href="https://youtu.be/dg27N2f8FAE?feature=shared">Watch</a></td></tr>
        <tr><td>55</td><td>Surah Ar Rahman</td><td><a href="https://youtu.be/5yG0N0v3F2Q?feature=shared">Watch</a></td></tr>
        <tr><td>56</td><td>Surah Al Waqiah</td><td><a href="https://youtu.be/39hctVQ_cVs?feature=shared">Watch</a></td></tr>
        <tr><td>57</td><td>Surah Al Hadid</td><td><a href="https://youtu.be/FSrg5Llo7qg?feature=shared">Watch</a></td></tr>
        <tr><td>58</td><td>Surah Al Mujadila</td><td><a href="https://youtu.be/_v5_kmdFg7A?feature=shared">Watch</a></td></tr>
        <tr><td>59</td><td>Surah Al Hashr</td><td><a href="https://youtu.be/Jp9rXj1FXp0?feature=shared">Watch</a></td></tr>
        <tr><td>60</td><td>Surah Al Mumtahanah</td><td><a href="https://youtu.be/Xgw2SZiqxMw?feature=shared">Watch</a></td></tr>
        <tr><td>61</td><td>Surah As Saff</td><td><a href="https://youtu.be/e2KhG5Z5w7k?feature=shared">Watch</a></td></tr>
        <tr><td>62</td><td>Surah Al Jumah</td><td><a href="https://youtu.be/6TZJntgTkD4?feature=shared">Watch</a></td></tr>
        <tr><td>63</td><td>Surah Al Munafiqun</td><td><a href="https://youtu.be/Qq9UQhxWHDI?feature=shared">Watch</a></td></tr>
        <tr><td>64</td><td>Surah At Taghabun</td><td><a href="https://youtu.be/XEKVgxH4_4Y?feature=shared">Watch</a></td></tr>
        <tr><td>65</td><td>Surah At Talaq</td><td><a href="https://youtu.be/QqFlxeq2GHs?feature=shared">Watch</a></td></tr>
        <tr><td>66</td><td>Surah At Tahrim</td><td><a href="https://youtu.be/0FUw7x0vQXM?feature=shared">Watch</a></td></tr>
        <tr><td>67</td><td>Surah Al Mulk</td><td><a href="https://youtu.be/Cj_M9oGQtnw?feature=shared">Watch</a></td></tr>
        <tr><td>68</td><td>Surah Al Qalam</td><td><a href="https://youtu.be/9j5zz-WG0P0?feature=shared">Watch</a></td></tr>
        <tr><td>69</td><td>Surah Al Haqqah</td><td><a href="https://youtu.be/b02huNrQFXw?feature=shared">Watch</a></td></tr>
        <tr><td>70</td><td>Surah Al Ma'arij</td><td><a href="https://youtu.be/KltwHzU1bhI?feature=shared">Watch</a></td></tr>
        <tr><td>71</td><td>Surah Nuh</td><td><a href="https://youtu.be/K7LskYZct30?feature=shared">Watch</a></td></tr>
        <tr><td>72</td><td>Surah Al Jin</td><td><a href="https://youtu.be/dOITuw_9Vck?feature=shared">Watch</a></td></tr>
        <tr><td>73</td><td>Surah Al Muzzammil</td><td><a href="https://youtu.be/KZ0cE-qlgXw?feature=shared">Watch</a></td></tr>
        <tr><td>74</td><td>Surah Al Mudathir</td><td><a href="https://youtu.be/f2z2cXj6Xq4?feature=shared">Watch</a></td></tr>
        <tr><td>75</td><td>Surah Al Qiyamah</td><td><a href="https://youtu.be/Qy0WqOykNKQ?feature=shared">Watch</a></td></tr>
        <tr><td>76</td><td>Surah Al Insan</td><td><a href="https://youtu.be/S3ipXvKn0Ac?feature=shared">Watch</a></td></tr>
        <tr><td>77</td><td>Surah Al Mursalat</td><td><a href="https://youtu.be/73VfSyJzFTQ?feature=shared">Watch</a></td></tr>
        <tr><td>78</td><td>Surah An Naba</td><td><a href="https://youtu.be/4AM6RxxwmOs?feature=shared">Watch</a></td></tr>
        <tr><td>79</td><td>Surah An Nazihat</td><td><a href="https://youtu.be/Zd0TYqFsbto?feature=shared">Watch</a></td></tr>
        <tr><td>80</td><td>Surah Abasa</td><td><a href="https://youtu.be/h1OvgG2s0X4?feature=shared">Watch</a></td></tr>
        <tr><td>81</td><td>Surah At Takwir</td><td><a href="https://youtu.be/PKpIz5RojZA?feature=shared">Watch</a></td></tr>
        <tr><td>82</td><td>Surah Al Infitar</td><td><a href="https://youtu.be/_DQpMnzRHwI?feature=shared">Watch</a></td></tr>
        <tr><td>83</td><td>Surah Al Mutaffifin</td><td><a href="https://youtu.be/zHDVVuyc7ro?feature=shared">Watch</a></td></tr>
        <tr><td>84</td><td>Surah Al Inshiqaq</td><td><a href="https://youtu.be/Z39R0kHH6eA?feature=shared">Watch</a></td></tr>
        <tr><td>85</td><td>Surah Al Buruj</td><td><a href="https://youtu.be/15UK6-vq0G8?feature=shared">Watch</a></td></tr>
        <tr><td>86</td><td>Surah At Tariq</td><td><a href="https://youtu.be/NhdzHg5vNcA?feature=shared">Watch</a></td></tr>
        <tr><td>87</td><td>Surah Al A'la</td><td><a href="https://youtu.be/X7c8bCqk5TQ?feature=shared">Watch</a></td></tr>
        <tr><td>88</td><td>Surah Al Ghashiya</td><td><a href="https://youtu.be/_gWsnv9n7ZI?feature=shared">Watch</a></td></tr>
        <tr><td>89</td><td>Surah Al Fajr</td><td><a href="https://youtu.be/qjgjY7tq5sQ?feature=shared">Watch</a></td></tr>
        <tr><td>90</td><td>Surah Al Balad</td><td><a href="https://youtu.be/3i6dr5RZth8?feature=shared">Watch</a></td></tr>
        <tr><td>91</td><td>Surah Ash Shams</td><td><a href="https://youtu.be/9jj_GRY5m_g?feature=shared">Watch</a></td></tr>
        <tr><td>92</td><td>Surah Al Layl</td><td><a href="https://youtu.be/m9_fqFkrX_w?feature=shared">Watch</a></td></tr>
        <tr><td>93</td><td>Surah Adh Dhuhah</td><td><a href="https://youtu.be/KzLihnLXmAI?feature=shared">Watch</a></td></tr>
        <tr><td>94</td><td>Surah Al Inshirah</td><td><a href="https://youtu.be/89BzYfgGxlM?feature=shared">Watch</a></td></tr>
        <tr><td>95</td><td>Surah At Tin</td><td><a href="https://youtu.be/ZxVJOlU6mZ4?feature=shared">Watch</a></td></tr>
        <tr><td>96</td><td>Surah Al Alaq</td><td><a href="https://youtu.be/X9TntAqGV7E?feature=shared">Watch</a></td></tr>
        <tr><td>97</td><td>Surah Al Qadr</td><td><a href="https://youtu.be/Du4YOw8XwPQ?feature=shared">Watch</a></td></tr>
        <tr><td>98</td><td>Surah Al Bayyina</td><td><a href="https://youtu.be/lc07uCF8b2Y?feature=shared">Watch</a></td></tr>
        <tr><td>99</td><td>Surah Az Zalzalah</td><td><a href="https://youtu.be/L3nb5oI6IfQ?feature=shared">Watch</a></td></tr>
        <tr><td>100</td><td>Surah Al Adiyat</td><td><a href="https://youtu.be/ehrOq0B0jTw?feature=shared">Watch</a></td></tr>
        <tr><td>101</td><td>Surah Al Qari'ah</td><td><a href="https://youtu.be/0XeNtcSV9S4?feature=shared">Watch</a></td></tr>
        <tr><td>102</td><td>Surah At Takathur</td><td><a href="https://youtu.be/V_6wnHq2biQ?feature=shared">Watch</a></td></tr>
        <tr><td>103</td><td>Surah Al Asr</td><td><a href="https://youtu.be/9Jrofa36Xtk?feature=shared">Watch</a></td></tr>
        <tr><td>104</td><td>Surah Al Humazah</td><td><a href="https://youtu.be/U71UlQma3dM?feature=shared">Watch</a></td></tr>
        <tr><td>105</td><td>Surah Al Fil</td><td><a href="https://youtu.be/9XkIC1_GAAk?feature=shared">Watch</a></td></tr>
        <tr><td>106</td><td>Surah Quraish</td><td><a href="https://youtu.be/YbwB3Xl3ph8?feature=shared">Watch</a></td></tr>
        <tr><td>107</td><td>Surah Al Ma'un</td><td><a href="https://youtu.be/q7O3f8JwzP8?feature=shared">Watch</a></td></tr>
        <tr><td>108</td><td>Surah Al Kauthar</td><td><a href="https://youtu.be/eTOm3Q16mQA?feature=shared">Watch</a></td></tr>
        <tr><td>109</td><td>Surah Al Kafirun</td><td><a href="https://youtu.be/ATpzgnIUVy8?feature=shared">Watch</a></td></tr>
        <tr><td>110</td><td>Surah An Nasr</td><td><a href="https://youtu.be/Qx8qLgz12nA?feature=shared">Watch</a></td></tr>
        <tr><td>111</td><td>Surah Al Masad</td><td><a href="https://youtu.be/_wqHDt6hfF0?feature=shared">Watch</a></td></tr>
        <tr><td>112</td><td>Surah Al Ikhlas</td><td><a href="https://youtu.be/2oHAlxuysZA?feature=shared">Watch</a></td></tr>
        <tr><td>113</td><td>Surah Al Falaq</td><td><a href="https://youtu.be/jfD97TrFkvY?feature=shared">Watch</a></td></tr>
        <tr><td>114</td><td>Surah An Nas</td><td><a href="https://youtu.be/b02huNrQFXw?feature=shared">Watch</a></td></tr>
        
st.markdown('</div>', unsafe_allow_html=True)


