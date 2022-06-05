import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
from PIL import Image
import math

# functions resposibble for the animation
# If we are using it localy
def load_lottie(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# if we are using it from url
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# FIND MORE EMOJIS HERE:https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Laser Safety Calculations", page_icon=':orange_book:', layout="wide")

# -------------SIDE BARS -----------------------
# -----------Using object notation--------------
add_selectbox = st.sidebar.selectbox(
    "-------------------------------MENU-----------------------------------",
    ('Home', "Maximum permissible exposure (MPE)", "Nominal Ocular Hazard Distance (NOHD)", "Nominal Hazard Zone (NHZ)")
)
if add_selectbox == "Maximum permissible exposure (MPE)":
    _left_column,midle_column,_right_column= st.columns(3)
    with midle_column:
        st.markdown("""<h1 style='text-align: center;
      width: 470px;
      height: 160px;
      border-radius: 50px;
      background-image: linear-gradient(yellow, orange);
      animation-name: example;
      animation-duration: 4s;'> Maximum Permissible Exposure (MPE) </h1>""",
                unsafe_allow_html=True)
    st.write('''<h3 style='text-align: center; color: grey;'> The MPE of a laser depends on the characteristics of 
    the laser and the time of exposure.MPE is the maximum level of laser radiation to which a person may be exposed
     without hazardous effects or biological changes in the eye or skin. The MPE is determined by the wavelength of 
     of laser, the energy involved, and the duration of the exposure. One of the most useful values in laser safety
    calculations is the Maximum Permissible Exposure (MPE). This is the irradiance or radiant exposure that may be 
    incident upon the eye (or the skin) without causing an adverse biological affect. The MPE varies by wavelength 
    and duration of exposure and is documented in tables published in ANSI z136.1 standard. We can think of this as 
    your laser safety speed limit. </h3>''', unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: grey;'>Continuous Wave Laser</h1>", unsafe_allow_html=True)

    with st.container():
        st.write("")
        left_column, right_column = st.columns(2)
        with left_column:
            st.latex(r'''
                                     eq.(1) MPE(H)=1.8t^{0.75}
                                     \frac{mJ}{cm^2} 
                                     ''')
            st.latex(r'''eq.(2):E= \frac{H}{t}  => ''')
            st.latex(r'''
                     eq.(3) MPE(E)= 
                     \frac{MPE(H)}{t}
                     ''')
            exposure_duration = st.number_input('Exposure duration in seconds.eq(1)')
            some_const = 1.8
            # by equation
            total_sum_mpe_joule = some_const * exposure_duration ** 0.75

        with right_column:
            with st.container():
                if total_sum_mpe_joule != 0:
                    total_sum_mpe_wats = total_sum_mpe_joule / exposure_duration


                    # st.latex(r'''MPE(H)=1.8t^{0.75}\frac{mJ}{cm^2}''')
                    # in order to interact with html file

                    class MPE:
                        first = f'{total_sum_mpe_joule:.3f}'
                        second = f'{total_sum_mpe_wats:.2f}'


                    # Read the HTML file
                    HTML_File = open('result_cont_wave.html', 'r')
                    result = HTML_File.read().format(first=MPE(), second=MPE())
                    st.write(result, unsafe_allow_html=True)

elif add_selectbox == "Nominal Ocular Hazard Distance (NOHD)":
    add_selectbox1 = st.sidebar.selectbox(
        "-------------------------------MENU-----------------------------------",
        ('NOHD for a lens on laser', "NOHD for a fiber laser: Multi-mode fibers",
         "NOHD for a fiber laser:Single-mode fibers")
    )

    left_column, middle_column, right_column = st.columns(3)

    with middle_column:
        st.markdown('''<h1 style='text-align: center;
          width: 500px;
          height: 160px;
          border-radius: 45px;
          background-image: linear-gradient(yellow, orange);
          animation-name: example;
          animation-duration: 4s;'>
         Nominal Ocular Hazard Distance (NOHD) </h1>''', unsafe_allow_html=True)

    st.write('''<h3 style='text-align: center; color: grey;'> NOHD sometimes referred to as the Nominal Hazard Distance,
        is the distance along the axis of emitted beam at which the ireradiance is equal to the MPE. The NOHD 
        is dependent on beam characteristics such as the power, diameter, and divergence.The NOHD is usually much 
        greater than the largest dimension of your laboratory space. </h3>''',
             unsafe_allow_html=True)
    with st.container():
        lefts_column, _right_column = st.columns(2)
        with lefts_column:
            formula_in_order = urllib.request.urlretrieve('https://github.com/D-on3/Streamlit_Laser_Safety_Calculations/blob/main/jpg/where_nohd.png',"where_nohd.png")
            image = Image.open(r'jpg\where_nohd.png')
            st.image(image)

    with st.container():
        mpe = 0
        f_emergent_beam_divergence = 0
        na_numerical_aperture_of_the_fiber = 0
        b0_diamter_of_beam = 0
        f_0_focal_lenght_lens = 0
        w_0_spot_size = 0
        p_0_power_of_the_laser = 0
        wavelenght = 0
        if add_selectbox1 == 'NOHD for a lens on laser':

            left_column, right_column = st.columns(2)
            first_nohd = 0

            with right_column:
                mpe = st.number_input('MPE value: mW')
                f_0_focal_lenght_lens = st.number_input('Focal length of a lens-f0')
                b0_diamter_of_beam = st.number_input("Diameter of beam incident on a focusing lens-b0")
                p_0_power_of_the_laser = st.number_input('Power of the laser Ф')

                if f_0_focal_lenght_lens > 0 and b0_diamter_of_beam > 0 and p_0_power_of_the_laser > 0 and mpe > 0:
                    try:

                        first_nohd = (f_0_focal_lenght_lens / b0_diamter_of_beam) * (
                                (p_0_power_of_the_laser / (math.pi * mpe)) ** 0.5)

                        class NOHD:
                            first_case = f'{first_nohd:.3f}'


                        HTML_File = open('result_nohd_1.html', 'r')
                        result = HTML_File.read().format(first=NOHD())

                    except ZeroDivisionError:
                        first_nohd = 0

            with left_column:
                st.write('NOHD for a lens on laser:')
                st.latex(r'''
                                                              NOHD(H)=\frac{f_0}{b_0}
                                                             \begin{bmatrix}
                           \left(\frac{4Ф}{\Pi MPE}\right)
                        \end{bmatrix}^{\frac{1}{2}} ''')

                if first_nohd > 0:
                    st.write(result, unsafe_allow_html=True)

            with left_column:
                # Read the HTML file
                pass
        elif add_selectbox1 == "NOHD for a fiber laser: Multi-mode fibers":
            second_nohd = 0
            left_column, right_column = st.columns(2)
            with right_column:
                mpe = st.number_input('MPE value: mW')
                na_numerical_aperture_of_the_fiber = st.number_input('Numerical aperture of the fiber')
                # f_0_focal_lenght_lens = st.number_input('Focal length of a lens-f0')
                # b0_diamter_of_beam = st.number_input("Diameter of beam incident on a focusing lens-b0")
                p_0_power_of_the_laser = st.number_input('Power of the laser Ф')

                if na_numerical_aperture_of_the_fiber > 0 and p_0_power_of_the_laser > 0 and mpe > 0:
                    try:
                        second_nohd = (1.7 / na_numerical_aperture_of_the_fiber) * (
                                (p_0_power_of_the_laser / (math.pi * mpe)) ** 0.5)
                        class NOHD:
                            first_case = f'{second_nohd:.3f}'


                        HTML_File = open('result_nohd_2.html', 'r')
                        result = HTML_File.read().format(first=NOHD())


                    except ZeroDivisionError:
                        second_nohd = 0
            with left_column:
                st.write('NOHD for a fiber laser:')
                st.latex(r'''
                                              NOHD(H)=\frac{1.7}{NA}
                                                                              \begin{bmatrix}
                                            \left(\frac{4Ф}{\Pi MPE}\right)
                                         \end{bmatrix}^{\frac{1}{2}} ''')

                if second_nohd > 0:
                    st.write(result, unsafe_allow_html=True)
                    # Read the HTML file


        elif add_selectbox1 == "NOHD for a fiber laser:Single-mode fibers":
            third_nohd = 0
            left_column, right_column = st.columns(2)
            with right_column:
                w_0_spot_size = st.number_input('Spot size of a single mode fiber')
                wavelenght = st.number_input('Wavelenght in nanometers')
                mpe = st.number_input('Maximum Permissible Exposure in mW/cm2')
                p_0_power_of_the_laser = st.number_input('power_of_the_laser')
                if w_0_spot_size > 0 and wavelenght > 0 and p_0_power_of_the_laser > 0 and mpe > 0:

                    try:
                        third_nohd = (w_0_spot_size / wavelenght) * (
                                ((math.pi * p_0_power_of_the_laser) / (2 * mpe)) * 0.5)


                        class NOHD:
                            first_case = f'{third_nohd:.3f}'
                        HTML_File = open('result_nohd_3.html', 'r')
                        result = HTML_File.read().format(first=NOHD())

                    except ZeroDivisionError:
                        third_nohd = 0

            with left_column:

                st.write('NOHD for a fiber laser:')
                st.latex(r'''
                      NOHD(H)=\frac{\omega_0}{\lambda}
                                                      \begin{bmatrix}
                    \left(\frac{\piФ}{2 MPE}\right)
                 \end{bmatrix}^{\frac{1}{2}} ''')
                # Read the HTML file
                if third_nohd > 0:
                    st.write(result, unsafe_allow_html=True)


elif add_selectbox == "Nominal Hazard Zone (NHZ)":
    _left_column, middle_column, _right_column = st.columns(3)
    with middle_column:
        st.write('''<h1 style='text-align: center;
          width: 500px;
          height: 160px;
          border-radius: 45px;
          background-image: linear-gradient(yellow, orange);
          animation-name: example;
          animation-duration: 4s;'>
           Nominal Hazard Zone (NHZ)</h1>''', unsafe_allow_html=True)
    st.write('''<h3 style='text-align: center; color: grey;'> The Nominal Hazard Zone (NHZ). This is a distance within
                which exposure to a direct, reflected, or scattered beam is greater than the MPE. Mirrors, optics, and 
                reflective materials in the beam path may result in diffuse or specular reflections in unintended 
                directions. Specular reflections are hazardous over a greater range than diffuse reflections. 
                If you are in the NHZ,
                you are at risk of an exposure above the MPE.</h3>
                <h3 style='text-align: center; color: grey;'>The NOHD is the dominant value for determining the radial extend of the NHZ if the bean be reasonably
expected to be incidentally directed towards people. The NHZ surrounding an optical set-up may be
calculated using the following formulas: </h3>''', unsafe_allow_html=True)
    left_column, right_column = st.columns(2)
    diffuse_reflection = 0
    specular_reflection = 0
    with right_column:
        spectral_reflectance = st.number_input(
            'ρl - the spectral reflectance of a diffuse or specular object at wavelength l')
        mpe = st.number_input('Maximum Permissible Exposure in mW/cm2')
        p_0_power_of_the_laser = st.number_input('Power of the laser Ф')
        reflection = st.number_input('θ- angle of reflection')
        f_emergent_beam_divergence = 0.001
        if spectral_reflectance > 0 and mpe > 0 and p_0_power_of_the_laser > 0 and reflection > 0:

            try:
                diffuse_reflection = (((spectral_reflectance * p_0_power_of_the_laser * math.cos(reflection))/
                                  (math.pi * mpe))**0.5)*10
                specular_reflection = ((1/f_emergent_beam_divergence)*((1.27 * spectral_reflectance
                                                                    * p_0_power_of_the_laser)/2.55)) ** 0.5

                specular_reflection = specular_reflection / 3.15608

                class NHZ:
                    first_case = f'{diffuse_reflection:.2f}'
                    second_case = f'{specular_reflection:.2f}'

                HTML_File = open('result_nhz.html', 'r')
                result = HTML_File.read().format(first=NHZ(),second=NHZ())

            except ZeroDivisionError:
                diffuse_reflection = 0
                specular_reflection = 0

    with left_column:
        #TODO: Formula-latex

        if diffuse_reflection != 0 and specular_reflection != 0:
            st.write(result, unsafe_allow_html=True)

else:

    left_column, middle_column, right_column = st.columns(3)

    with left_column:
        animation = load_lottie_url('https://assets8.lottiefiles.com/private_files/lf30_jpe6wzcq.json')
        st_lottie(animation, height=200, key='134')

    with middle_column:
        st.markdown('''<h1 style='text-align: center;
      width: 470px;
      height: 160px;
      border-radius: 50px;
      background-image: linear-gradient(yellow, orange);
      animation-name: example;
      animation-duration: 4s;'>
    LASER SAFETY CALCULATIONS </h1>''' , unsafe_allow_html=True)

    with right_column:
        animation = load_lottie_url('https://assets8.lottiefiles.com/private_files/lf30_jpe6wzcq.json')
        st_lottie(animation, height=200, key='122')

    left_column, right_column = st.columns(2)
    with left_column:

        st.markdown("""<h3 style='text-align: center; color: grey;'>
        The human body is vulnerable to the output of certain lasers, and under certain circumstances, exposure can
         result in damage to the eye and skin. Research relating to
    injury thresholds of the eye and skin has been carried out in order to understand the biological hazards of laser
    radiation. The primary objective of the laser safety program is
    to ensure that no laser radiation in excess of the maximum permissible exposure (MPE) limit reaches the human eye 
    or skin.</h3>""", unsafe_allow_html=True)
    with right_column:
        st.markdown('''<h3 style='text-align: center; color: grey;'> Additionally, the program is designed to ensure 
        that adequate protection against collateral hazards is 
    provided. These collateral hazards include the risk of electrical shock, fire hazard from a beam or from use of dyes
    and solvents, and chemical exposures from use of chemicals and vaporization of targets.</h3>''' ,
                    unsafe_allow_html=True)
    st.write('''<h3 style='text-align: center; color: grey;'> If I can be of assistance, please do not hesitate to contact me</h3>''',
                 unsafe_allow_html=True)

    st.write('''<h3 style='text-align: center; color: grey;'>
                If you have suggestions , or some recommendations for extending the functionality of this calculator or
                have some other idea. Please let me know if you have further questions on this matter. If you experience
                any further problems, please feel free to contact me. </h3>''',unsafe_allow_html=True)


    # st.markdown(social_media, unsafe_allow_html=True)

    with st.container():

        left_column, middle_column_column, right_column = st.columns(3)

        with left_column:

            contact = load_lottie_url('https://assets1.lottiefiles.com/packages/lf20_lshv4smz.json')
            st_lottie(contact, height=500, key='4')
        with right_column:

            contact = load_lottie_url('https://assets1.lottiefiles.com/packages/lf20_lshv4smz.json')
            st_lottie(contact, height=500, key='3')
        with middle_column_column:
            # ---- CONTACT ----
            contact_form = """

<head>
    <meta charset="UTF-8">
    <style>
    .container {
  height: 480px;
  width: 350px;
  position: centered;
  background-image: linear-gradient(#7ED321, #F5A623);
  border-radius: 25px;
  padding: 18px;
  border: 2px solid #7ED321;
}
        .button:hover {

  opacity: 0.7;
  background-image: linear-gradient(yellow, lime );
}
    </style>
</head>
<body>
<div  class="container">


            <form action="https://formsubmit.co/330659a1fbcf955e6728859239fc1888" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input style="color: grey;  width: 100%;padding: 12px;border: 2px solid #7ED321; border-radius: 15px;
                box-sizing: border-box; margin-top: 6px; margin-bottom: 16px; resize:none;" type="text" name="name"
                       placeholder="Your name" required >
                <br><input style="color: grey;  width: 100%;padding: 12px;border: 2px solid #7ED321; border-radius: 15px;
                box-sizing: border-box; margin-top: 6px; margin-bottom: 16px; resize:none;" type="email" name="email" placeholder="Your email" required >
                <br><textarea style="color: grey; height: 270px; width: 100%;padding: 12px;border: 2px solid #7ED321; border-radius: 15px;
                box-sizing: border-box; margin-top: 6px; margin-bottom: 16px; resize:none" name="message" placeholder="Your message here" required >
                </textarea>


    <button class = 'button' style="color: black ; width : 120px; height:50px; border-radius: 25px; margin: 0;
  position: absolute;
  top: 90%;
  left: 42%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);border: 2px solid yellowgreen;" type="submit"> Send </button>

            </form>
</div>
</body>
            """

            # ---Contact form---init
            components.html(contact_form, height=550, scrolling=False)
        social_media = '''<head>
                                    <meta name="viewport" content="width=device-width, initial-scale=1">
                                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
                                    <style>
                                    .fa {
                                      margin = 0;
                                      padding: 25px;
                                      font-size: 30px;
                                      width: 20px;
                                      height: 20px;
                                      text-align: center;
                                      text-decoration: none;
                                      margin: 15px 15px;


                                    }

                                    .fa:hover {
                                        opacity: 0.7;
                                    }

                                    </style>
                                    </head>
                                    <body>
                                    <div class="container">
                                    <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
                                    <a style = '                                   margin: 0;
                                    position: absolute;
  top: 10%;
  left: 60%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);'' href="https://github.com/D-on3" class="fa fa-github">GitHub</a>
                                    <a  style = 'margin: 0; position: absolute;top: 10%;left: 80% -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);'href="https://www.facebook.com/profile.php?id=100004700626557" class="fa fa-facebook">acebook</a>
                                    </div>
                                    </body>'''

        final_lef_column,final_midle_column,final_right_column=st.columns(3)
        with final_midle_column:
            components.html(social_media, height=250)

