import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
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


add_selectbox = st.sidebar.selectbox('MENU', (
    'Home', "Maximum permissible exposure (MPE)", "Nominal Ocular Hazard Distance (NOHD)", "Nominal Hazard Zone (NHZ)"))
if add_selectbox == "Maximum permissible exposure (MPE)":
    _left_column, midle_column, _right_column = st.columns(3)
    with midle_column:
        st.markdown('''<h3 style='
         display: block;
         margin-left: auto;
         margin-right: auto;
        text-align: center;
             width: 300px;
             height: 90px;
             border-radius: 45px;
             background-image: linear-gradient(yellow, orange);
             animation-name: example;
             animation-duration: 4s;'>
           Maximum Permissible Exposure (MPE) </h3>''', unsafe_allow_html=True)

    st.write('''<h5 style='text-align: center; color: grey;'> The MPE of a laser depends on the characteristics of 
    the laser and the time of exposure.MPE is the maximum level of laser radiation to which a person may be exposed
     without hazardous effects or biological changes in the eye or skin. The MPE is determined by the wavelength of 
     of laser, the energy involved, and the duration of the exposure. One of the most useful values in laser safety
    calculations is the Maximum Permissible Exposure (MPE). This is the irradiance or radiant exposure that may be 
    incident upon the eye (or the skin) without causing an adverse biological affect. The MPE varies by wavelength 
    and duration of exposure and is documented in tables published in ANSI z136.1 standard. We can think of this as 
    your laser safety speed limit. </h5>''', unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center; color: grey;'>Continuous Wave Laser</h3>", unsafe_allow_html=True)

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
        "MENU",
        ('NOHD for a lens on laser', "NOHD for a fiber laser: Multi-mode fibers",
         "NOHD for a fiber laser:Single-mode fibers")
    )

    left_column, middle_column, right_column = st.columns(3)

    with middle_column:
        st.markdown('''<h3 style='
         display: block;
         margin-left: auto;
         margin-right: auto;
        text-align: center;
             width: 300px;
             height: 90px;
             border-radius: 45px;
             background-image: linear-gradient(yellow, orange);
             animation-name: example;
             animation-duration: 4s;'>
           Nominal Ocular Hazard Distance (NOHD) </h3>''', unsafe_allow_html=True)

    st.write('''<h5 style='text-align: center; color: grey;'> NOHD sometimes referred to as the Nominal Hazard Distance,
        is the distance along the axis of emitted beam at which the ireradiance is equal to the MPE. The NOHD 
        is dependent on beam characteristics such as the power, diameter, and divergence.The NOHD is usually much 
        greater than the largest dimension of your laboratory space. </h5>''',
             unsafe_allow_html=True)
    with st.container():
        lefts_column, _right_column = st.columns(2)
        with lefts_column:
            pass

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
        st.markdown('''<h3 style='
         display: block;
         margin-left: auto;
         margin-right: auto;
        text-align: center;
             width: 300px;
             height: 90px;
             border-radius: 45px;
             background-image: linear-gradient(yellow, orange);
             animation-name: example;
             animation-duration: 4s;'>
          Nominal Hazard Zone (NHZ) </h3>''', unsafe_allow_html=True)

    st.write('''<h5 style='text-align: center; color: grey;'> The Nominal Hazard Zone (NHZ). This is a distance within
                which exposure to a direct, reflected, or scattered beam is greater than the MPE. Mirrors, optics, and 
                reflective materials in the beam path may result in diffuse or specular reflections in unintended 
                directions. Specular reflections are hazardous over a greater range than diffuse reflections. 
                If you are in the NHZ,
                you are at risk of an exposure above the MPE.</h5>
                <h5 style='text-align: center; color: grey;'>The NOHD is the dominant value for determining the radial extend of the NHZ if the bean be reasonably
expected to be incidentally directed towards people. The NHZ surrounding an optical set-up may be
calculated using the following formulas: </h5>''', unsafe_allow_html=True)
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
                diffuse_reflection = (((spectral_reflectance * p_0_power_of_the_laser * math.cos(reflection)) /
                                       (math.pi * mpe)) ** 0.5) * 10
                specular_reflection = ((1 / f_emergent_beam_divergence) * ((1.27 * spectral_reflectance
                                                                            * p_0_power_of_the_laser) / 2.55)) ** 0.5
                # Todo: There is an error in the calculations.
                specular_reflection = specular_reflection / 3.15608


                class NHZ:
                    first_case = f'{diffuse_reflection:.2f}'
                    second_case = f'{specular_reflection:.2f}'


                HTML_File = open('result_nhz.html', 'r')
                result = HTML_File.read().format(first=NHZ(), second=NHZ())

            except ZeroDivisionError:
                diffuse_reflection = 0
                specular_reflection = 0

    with left_column:
        # TODO: Formula-latex
        st.latex(r'''r_{NHZ}=\left(\frac{\rho_\lambda Ф\cos\theta}{\pi MPE}\right)^{\frac{1}{2}}
                                                                     ''')
        st.latex(r'''r_{NHZ}=\frac{1}{\phi}\left(\frac{1.27\rho_\lambda Ф}{MPE}\right)^{\frac{1}{2}} ''')

        if diffuse_reflection != 0 and specular_reflection != 0:
            st.write(result, unsafe_allow_html=True)

else:

    left_column, middle_column, right_column = st.columns(3)

    with left_column:
        animation = load_lottie_url('https://assets8.lottiefiles.com/private_files/lf30_jpe6wzcq.json')
        st_lottie(animation, height=90, key='134')

    with middle_column:
        st.markdown('''<h3 style='
         display: block;
         margin-left: auto;
         margin-right: auto;
        text-align: center;
             width: 300px;
             height: 90px;
             border-radius: 45px;
             background-image: linear-gradient(yellow, orange);
             animation-name: example;
             animation-duration: 4s;'>
           LASER SAFETY CALCULATIONS </h3>''', unsafe_allow_html=True)

    with right_column:
        animation = load_lottie_url('https://assets8.lottiefiles.com/private_files/lf30_jpe6wzcq.json')
        st_lottie(animation, height=90, key='122')

    left_column, right_column = st.columns(2)
    with left_column:

        st.markdown("""<h5 style='text-align: center; color: grey;'>
        The human body is vulnerable to the output of certain lasers, and under certain circumstances, exposure can
         result in damage to the eye and skin. Research relating to
    injury thresholds of the eye and skin has been carried out in order to understand the biological hazards of laser
    radiation. The primary objective of the laser safety program is
    to ensure that no laser radiation in excess of the maximum permissible exposure (MPE) limit reaches the human eye 
    or skin.</h5>""", unsafe_allow_html=True)
    with right_column:
        st.markdown('''<h5 style='text-align: center; color: grey;'> Additionally, the program is designed to ensure 
        that adequate protection against collateral hazards is 
    provided. These collateral hazards include the risk of electrical shock, fire hazard from a beam or from use of dyes
    and solvents, and chemical exposures from use of chemicals and vaporization of targets.</h5>''',
                    unsafe_allow_html=True)
    _left_column, midle_column, _right_column = st.columns(3)
    with midle_column:
        st.write(
            '''<h5 style='text-align: center; color: grey;'> If I can be of assistance, please do not hesitate to contact me</h5>''',
            unsafe_allow_html=True)

        st.write('''<h5 style='text-align: center; color: grey;'>
                If you have suggestions , or some recommendations for extending the functionality of this calculator or
                have some other idea. Please let me know if you have further questions on this matter. If you experience
                any further problems, please feel free to contact me. </h5>''', unsafe_allow_html=True)

    # st.markdown(social_media, unsafe_allow_html=True)

    with st.container():

        contact_form = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
            <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>

<script type="text/javascript">
    document.getElementById("btn").onclick = function () {
        location.href = "www.google.com";
    };
</script>


    <title>Title</title>
    <style>
    :root {



  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 65%;
    font-size: 62.5%;


}

* {
    box-sizing: border-box;
    font-family: Arial, Helvetica, sans-serif;
    margin: 0
    padding: 0;
    color: black;
}


h1,
h2,
h3,
h4 {
    margin-bottom: 1rem;

}


h1 > span {
    font-size: 2.4rem;
    font-weight: 500;
}

h1 {
    font-size: 3.4rem;
    margin-bottom: 2.2rem;
    font-weight: 700;
    color: white;
    padding: 10px;
    background-image: linear-gradient(powderblue, darkblue);
    border-radius: 15px;


}

h2 {
    font-size: 4.2rem;
    margin-bottom: 2.2rem;
    font-weight: 700;
}

h3 {
    font-size: 2.2rem;
    margin-bottom: 2.2rem;
    font-weight: 500;
}


.holders {
    width: 100vw;
    height: 90vh;
    position: centered;
    border-radius: 25px;

    padding: 18px;
    display: flex;
    justify-content: center;
    align-items: center;
    max-width: 80rem;
    margins: 0 auto;
    opacity: 1.5;
}


.contact{
    width: 300px;
    height:420px;
    border: 1px solid #ffe605;
    background-image:radial-gradient(white, #ffe605);
    align-items: center;

    border-radius: 25px;
    opacity: 1;
    padding: 8px;





}

/*Utilities*/


}

.container  {
    width: 100%;

}

.flex-center {
    display: flex;
    flex-direction: column;
}

.flex-center {
    justify-content: center;
    align-items: center;
}

.justify-center {
    justify-content: center;

}

.text-center {
    text-align: center;
}

.hidden {
    display: none;

}

#input_name,
#input_email{
    color: grey;
    width: 100%;
    padding:12px;
    border: 2px #F5A623;
    border-radius: 15px;
    margin-top: 6px;
    margin-bottom: 6px;
    box-sizing: border-box;
    resize:none;

}
#input_msg{

    color: grey;
    width: 100%;
    padding: 5px;
    border-radius: 15px;
    width: 100%;
    height: 230px;
    margin-top: 5px;
    resize:none;
    border: 1px solid #ffe605;
}
/*Buttons*/


.btn {
    position: absolute;
    z-index: 1;
    font-size: 1.8rem;
    padding: 1rem 0;
    width: 20rem;
    text-align: center;
    text-decoration: none;
    color: #995300;
    border: 3px solid #ffe400;
    border-radius: 35px;
     background-image:radial-gradient(#ffe605,white);
    margin-top: 5px;
    margin-left: 30px;
}

.btn:hover{
    cursor: pointer;
    box-shadow:: 0 1.4rem 0 rgba(86, 185, 235, 0.5);
    transform: translateY(-0.1rem);
    transition: transform 150ms;

}


.btn[disabled]:hover {
    cursor: not-allowed;
    box-shadow: none;
    transform: none;

}

.lot{

        position: fixed;
    z-index: -1;
    margin-right: 10px;
    width: 700px;
    height: 700px;
    margin-bottom: 40px;
    opacity: 0.95;
}
.lot1{
    transform: rotate(180deg);
        position: fixed;
    z-index: -1;
    margin-right: 10px;
    width: 750px;
    height: 750px;
    margin-bottom: -50px;
    opacity: 0.95;
}
    </style>
 <link rel="stylesheet"href="scratch.css">
</head>
<body>

<div  class="container">

        <div class="holders">
            <!---https://lottiefiles.com/69964-nature-contact-->
            <lottie-player class = 'lot' src="https://assets9.lottiefiles.com/packages/lf20_lshv4smz.json"  background="transparent"  speed="1"  loop  autoplay></lottie-player>

            <div class="contact">
            <form action="https://formsubmit.co/330659a1fbcf955e6728859239fc1888" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <br><input  id = 'input_name' type="text" name="name" placeholder="Your name" required >
                <br><input  id = 'input_email' type="email" name="email" placeholder="Your email" required >

                <br><textarea id = 'input_msg' name="message" placeholder="Your message here" required >
                </textarea><br>

<!--css text area  style ='color: grey;  width: 100%;padding: 12px;border: 5px solid yellowgreen; border-radius: 15px;
                box-sizing: border-box; margin-top: 6px; margin-bottom: 16px; resize:none;'-->

               <button id = 'btn' onclick='myhref()' = 'contact_form.html' " class = 'btn' type="submit"> Send </button>


            </form>
            </div>>

            <!--<lottie-player class = 'lot1' src="https://assets9.lottiefiles.com/packages/lf20_lshv4smz.json"  background="transparent"  speed="1"  loop  autoplay></lottie-player>-->
        </div>
</div>



</body>
</html>
            """




        # ---Contact form---init
        components.html(contact_form, height=550, scrolling=False)
