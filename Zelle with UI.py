import pygame as pg
import json
import sys
import time
import os


background=(0,100,0)          #COLORS
color=(220,190,30)
color2=(163,73,164)
color3=(50,100,240)
color4=(106,222,225)

list_of_buttons = [] #tiene que generarse con cada ventana



width  = 550                #SCREEN PROPORTIONS
height = 620

pg.init()

try:
    with open("Prob.json") as file:
            data_base = json.load(file)
except:
    print("Hubo un problema ejecutando el sistema\n")
    exit()

menu_font = pg.font.SysFont("Siemens Slab Black", 30)
welc_font = pg.font.SysFont("Siemens Slab Black", 20)
inst_font = pg.font.SysFont("Siemens Slab Black", 17)
bot_font = pg.font.SysFont("Siemens Slab Black", 15)

def setup ():
    
    global screen
    global background_filling
    screen = pg.display.set_mode((width,height))
    pg.display.set_caption('Zelle')
    background_filling = pg.image.load(r'BackGroundZelle.jpg')
    zelle_icon = pg.image.load(r'ICONS.png')
    screen.blit(background_filling, (0, 0))
    pg.display.set_icon(zelle_icon) 
    pg.display.update()

def clear_screen():
    
    global screen, background_filling
    tag = "Bienvenido a Zelle,"
    tag1 = "por favor siga las instrucciones"
    tag2 = "que aparecen en el recuadro de abajo"
    screen.blit(background_filling, (0, 0))
    label=welc_font.render(tag, 1, color3)
    label1=welc_font.render(tag1, 1, color3)
    label2=welc_font.render(tag2, 1, color3)
    screen.blit(label, (65,65))
    screen.blit(label1, (65,85))
    screen.blit(label2, (65,105))

    bot_but()
    
    pg.display.update()

def button( posx, posy, sizx, sizy, name):

    tag = name
    x_size = sizx
    y_size = sizy
    x_pos = posx
    y_pos = posy
    tag_lenght = len(tag)
    x_tag = abs(tag_lenght*20 - x_size)/2 + x_pos + 5
    y_tag = abs(36 - y_size)/2 + y_pos
    pg.draw.rect(screen,(100,0,100),(x_pos,y_pos,x_size,y_size))
    label=menu_font.render(tag, 1, color4)
    screen.blit(label, (x_tag,y_tag))
    pg.display.update()
    return [(x_size,y_size),(x_pos, y_pos),tag] # <----- esto es un button en if clicked

def number_box(num):
    global screen
    tag = num
    
    x_tag = 350 - 9*len(tag)
    pg.draw.rect(screen,(0,0,0),(200,300,300,60))
    pg.draw.rect(screen,(255,255,255),(205,305,290,50))
    label=menu_font.render(tag, 1, color3)
    screen.blit(label, (x_tag,312))
    pg.display.update()
    
    if len(tag) == 14:
        
        return False
    else:
        
        return True

def if_clicked (x_mouse_pos, y_mouse_pos):

    if len(list_of_buttons) > 0 :

        for button in list_of_buttons:

            if (x_mouse_pos- button[1][0]) < button[0][0] and (y_mouse_pos- button[1][1]) < button[0][1] :
                
                if (x_mouse_pos- button[1][0]) > 0 and (y_mouse_pos- button[1][1]) > 0 :

                    if button [2] == 'Salir':
                        
                        pg.display.quit()
                        sys.exit()

                    hide_buttons()

                    clear_screen()
                    
                    return button [2]
                
        return "None"



def call_buttons ( amount, names ):

    global list_of_buttons


    y = 300

    for i in range (0, amount):
    
        list_of_buttons.append(button(200,y,300,60, names[i]))
        y = y + 100

def bot_but ():

    global list_of_buttons

    pg.draw.rect(screen,(100,0,100),(422,580,60,20))
    label=bot_font.render("Salir", 1, color4)
    screen.blit(label, (434,580))

    pg.draw.rect(screen,(100,0,100),(220,580,80,20))
    label=bot_font.render("Regresar", 1, color4)
    screen.blit(label, (226,580))

    list_of_buttons.append([(60,20),(422,580),"Salir"])
    list_of_buttons.append([(80,20),(220,580),"Regresar"])
     

def hide_buttons():

    global list_of_buttons

    list_of_buttons = []
    
def main_loop ():
    
    loop = True
    left_click = 0

    while loop:

        event_list = pg.event.get()

        for event in event_list:
            
            if event.type == pg.QUIT:
                time.sleep(0.5)
                pg.display.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                
                buttons = pg.mouse.get_pressed()
                left_click = buttons[0]
                    
            if event.type == pg.MOUSEBUTTONUP:

                summ = 0
                mouse_pos = pg.mouse.get_pos()
                for a in buttons:
                    summ = summ + a
                    
                if left_click == 1 and summ == 1:
                    selection = if_clicked (mouse_pos[0], mouse_pos[1])
                    if selection != "None":
                       return selection

def number_loop ():

    loop = True
    left_click = 0
    number_string = "0"
    number_int = 0
    limit = True

    while loop:

        event_list = pg.event.get()

        for event in event_list:
            
            if event.type == pg.QUIT:
                time.sleep(0.5)
                pg.display.quit()
                sys.exit()

            if event.type == pg.KEYUP:

                limit = number_box(number_string)

            if event.type == pg.KEYDOWN:

            
                if (event.key == pg.K_KP0 or event.key == pg.K_0) and limit:
                
                    number_string = number_string + "0"
                    number_int = int(number_string)
                    
                    if number_int == 0:
                        number_string = "0"
                    
                if (event.key == pg.K_KP1 or event.key == pg.K_1) and limit:
                    
                    number_int = int(number_string)
                    
                    if number_int == 0:
                        
                        number_string = ""
                        
                    number_string = number_string + "1"
                    
                if (event.key == pg.K_KP2 or event.key == pg.K_2) and limit:

                    number_int = int(number_string)
                    
                    if number_int == 0:
                        
                        number_string = ""
                
                    number_string = number_string + "2"
                    
                if (event.key == pg.K_KP3 or event.key == pg.K_3) and limit:

                    number_int = int(number_string)
                    
                    if number_int == 0:
                        
                        number_string = ""
                    
                    number_string = number_string + "3"
                    
                if (event.key == pg.K_KP4 or event.key == pg.K_4) and limit:

                    number_int = int(number_string)
                    
                    if number_int == 0:
                        
                        number_string = ""
                
                    number_string = number_string + "4" 
                    
                if (event.key == pg.K_KP5 or event.key == pg.K_5) and limit:

                    number_int = int(number_string)
                    
                    if number_int == 0:
                        
                        number_string = ""
                
                    number_string = number_string + "5"
                    
                if (event.key == pg.K_KP6 or event.key == pg.K_6) and limit:

                    number_int = int(number_string)
                    
                    if number_int == 0:
                        
                        number_string = ""
                
                    number_string = number_string + "6"               
                    
                if (event.key == pg.K_KP7 or event.key == pg.K_7) and limit:

                    number_int = int(number_string)
                    
                    if number_int == 0:
                        
                        number_string = ""
                
                    number_string = number_string + "7"
                    
                if (event.key == pg.K_KP8 or event.key == pg.K_8) and limit:

                    number_int = int(number_string)
                    
                    if number_int == 0:
                        
                        number_string = ""
                
                    number_string = number_string + "8"
                    
                if (event.key == pg.K_KP9 or event.key == pg.K_9) and limit:

                    number_int = int(number_string)
                    
                    if number_int == 0:
                        
                        number_string = ""
                
                    number_string = number_string + "9"
                     

                if event.key == pg.K_BACKSPACE or event.key == pg.K_DELETE:

                    if len(number_string) == 1:
                        
                        number_string = "0"

                    else:
                        number_string = number_string[:-1]


                if event.key == pg.K_KP_ENTER or event.key == pg.K_RETURN:

                    if int(number_string)<= 100:

                        number_int = int(number_string)

                        return number_int
                    
            if event.type == pg.MOUSEBUTTONDOWN:
                
                buttons = pg.mouse.get_pressed()
                left_click = buttons[0]
                    
            if event.type == pg.MOUSEBUTTONUP:

                summ = 0
                mouse_pos = pg.mouse.get_pos()
                for a in buttons:
                    summ = summ + a
                    
                if left_click == 1 and summ == 1: #Aqui debe llamarse la funcion para verificar que boton se cliqueo
                    selection = if_clicked (mouse_pos[0], mouse_pos[1])
                    if selection == 'Regresar':
                        selection = 756
                    if selection != 'None':
                        return selection

def Main_menu ():

    clear_screen()

    inst = "Selecciona la zona de donde"
    inst2  = "fue extraida tu muestra citológica"
    selection = ""
    
    label=inst_font.render(inst, 1, color2)
    label1=inst_font.render(inst2, 1, color2)
    screen.blit(label, (195,200))
    screen.blit(label1, (195,220))
    
    names = ["Exocérvix","Endocérvix","Z. de transición"]

    amount = len(names)

    call_buttons ( amount, names )

    selection = main_loop ()
    
    
    if selection == 'Exocérvix':
        Exocervix ()
            
    elif selection == 'Endocérvix':
        Endocervix ()
        
    elif selection == 'Z. de transición':
        Transition_zone ()

    Main_menu()

def Exocervix():

    clear_screen()

    inst = "Selecciona la edad reproductiva"
    inst2  = "de la paciente en cuestión"
    selection = ""
    
    label=inst_font.render(inst, 1, color2)
    label1=inst_font.render(inst2, 1, color2)
    screen.blit(label, (195,200))
    screen.blit(label1, (195,220))
    
    names = ["Reproductiva"," No reproductiva"]

    amount = len(names)

    call_buttons ( amount, names )

    selection = main_loop ()

    
    if selection == 'Reproductiva':
        Reproductive ()
            
    elif selection == ' No reproductiva':
        Non_reproductive ()

    elif selection == 'Regresar':
        return
    
def Reproductive ():
    
    ExoR_probs_IS_CS = []
    ExoR_probs_IV_CS = []
    ExoR_probs_SS_CS = []
    ExoR_probs_SV_CS = []
    
    ExoR_probs_IS_NS = []
    ExoR_probs_IV_NS = []
    ExoR_probs_SS_NS = []
    ExoR_probs_SV_NS = []

    P_data_IntS_Cit = 0.063
    P_data_IntV_Cit = 0.472
    P_data_SupS_Cit = 0.38
    P_data_SupV_Cit = 0.047 
    P_data_IntS_Nuc = 0.06
    P_data_IntV_Nuc = 0.47
    P_data_SupS_Nuc = 0.25
    P_data_SupV_Nuc = 0.049

    clear_screen()

    inst = "Indique el tamaño promedio"
    inst2  = "del citoplasma de las células"
    selection = ""

    label=inst_font.render(inst, 1, color2)
    label1=inst_font.render(inst2, 1, color2)
    screen.blit(label, (195,195))
    screen.blit(label1, (195,215))

    number_box("0")

    number = number_loop ()
    

    if number < 12:  
        ExoR_probs_IS_CS.append(0.05)
        ExoR_probs_IV_CS.append(0.01)

    if number >= 12 and number <=20:
        ExoR_probs_IS_CS.append(0.80)
        ExoR_probs_IV_CS.append(0.01)
        
    if number > 20 and number < 70 :
        ExoR_probs_IS_CS.append(0.15)
        ExoR_probs_IV_CS.append(0.01)

    if number < 20:  
        ExoR_probs_SS_CS.append(0.05)
        ExoR_probs_SV_CS.append(0.01)

    if number >= 20 and number <=35:
        ExoR_probs_SS_CS.append(0.75)
        ExoR_probs_SV_CS.append(0.01)
        
    if number > 35 and number < 70 :
        ExoR_probs_SS_CS.append(0.20)
        ExoR_probs_SV_CS.append(0.01)

    if number >= 70:
        ExoR_probs_IV_CS.append(1.00)
        ExoR_probs_SV_CS.append(1.00)
        ExoR_probs_IS_CS.append(0.01)
        ExoR_probs_SS_CS.append(0.01)
        
    if number == 756:
        return
                    

    clear_screen()

    inst = "Indique el tamaño promedio"
    inst2  = "del núcleo de las células"
    selection = ""

    label=inst_font.render(inst, 1, color2)
    label1=inst_font.render(inst2, 1, color2)
    screen.blit(label, (195,195))
    screen.blit(label1, (195,215))

    number_box("0")

    number = number_loop ()
    
    if number < 9:
        ExoR_probs_IS_NS.append(0.08)
        ExoR_probs_IV_NS.append(0.01)

    if number >= 9  and number <=11:
        ExoR_probs_IS_NS.append(0.75)
        ExoR_probs_IV_NS.append(0.01)
        
    if number > 11 and number < 20:
        ExoR_probs_IS_NS.append(0.17)
        ExoR_probs_IV_NS.append(0.01)

    if number < 7:
        ExoR_probs_SS_NS.append(0.36)
        ExoR_probs_SV_NS.append(0.01)

    if number >= 7 and number <=11:
        ExoR_probs_SS_NS.append(0.53)
        ExoR_probs_SV_NS.append(0.01)
        
    if number > 11 and number < 20:
        ExoR_probs_SS_NS.append(0.11)
        ExoR_probs_SV_NS.append(0.01)

    if number >= 20:
        ExoR_probs_IV_NS.append(1.00)
        ExoR_probs_SV_NS.append(1.00)
        ExoR_probs_IS_NS.append(0.01)
        ExoR_probs_SS_NS.append(0.01)

    if number == 756:
        return
    
    clear_screen()

    inst = "Las características de"
    inst2  = "su muestra indican que:"
    selection = ""

    label=inst_font.render(inst, 1, color2)
    label1=inst_font.render(inst2, 1, color2)
    screen.blit(label, (195,200))
    screen.blit(label1, (195,220))

    pg.display.update()
    
    #calculo de probabilidades con teorema de bayes
    likelyhood = 1    #Intermedia sana por citoplas******************************************

    for probability in data_base["Exo R"]["Int Sana"]:
        ExoR_probs_IS_CS.append(probability)
        
    for probability in ExoR_probs_IS_CS:
        likelyhood = likelyhood * probability

    bayes_prob_IS_CS = (likelyhood / P_data_IntS_Cit) * 100
    
    likelyhood = 1    #Intermedia  VPH por citoplas******************************************

    for probability in data_base["Exo R"]["Int VPH"]:
        ExoR_probs_IV_CS.append(probability)
        
    for probability in ExoR_probs_IV_CS:
        likelyhood = likelyhood * probability

    bayes_prob_IV_CS = (likelyhood / P_data_IntV_Cit) * 100
    
    likelyhood = 1    #Superficial sana por citoplas******************************************

    for probability in data_base["Exo R"]["Sup Sana"]:
        ExoR_probs_SS_CS.append(probability)
        
    for probability in ExoR_probs_SS_CS:
        likelyhood = likelyhood * probability

    bayes_prob_SS_CS = (likelyhood / P_data_SupS_Cit) * 100
    
    likelyhood = 1    #Superficial VPH por citoplas******************************************

    for probability in data_base["Exo R"]["Sup VPH"]:
        ExoR_probs_SV_CS.append(probability)
        
    for probability in ExoR_probs_SV_CS:
        likelyhood = likelyhood * probability

    bayes_prob_SV_CS = (likelyhood / P_data_SupV_Cit) * 100

    likelyhood = 1    #Intermedia sana por nucleo******************************************

    for probability in data_base["Exo R"]["Int Sana"]:
        ExoR_probs_IS_NS.append(probability)
        
    for probability in ExoR_probs_IS_NS:
        likelyhood = likelyhood * probability

    bayes_prob_IS_NS = (likelyhood / P_data_IntS_Nuc) * 100
    
    likelyhood = 1    #Intermedia  VPH por nucleo******************************************

    for probability in data_base["Exo R"]["Int VPH"]:
        ExoR_probs_IV_NS.append(probability)
        
    for probability in ExoR_probs_IV_NS:
        likelyhood = likelyhood * probability

    bayes_prob_IV_NS = (likelyhood / P_data_IntV_Nuc) * 100
    
    likelyhood = 1    #Superficial sana por nucleo******************************************

    for probability in data_base["Exo R"]["Sup Sana"]:
        ExoR_probs_SS_NS.append(probability)
        
    for probability in ExoR_probs_SS_NS:
        likelyhood = likelyhood * probability

    bayes_prob_SS_NS = (likelyhood / P_data_SupS_Nuc) * 100
    
    likelyhood = 1    #Superficial VPH por nucleo******************************************

    for probability in data_base["Exo R"]["Sup VPH"]:
        ExoR_probs_SV_NS.append(probability)
        
    for probability in ExoR_probs_SV_NS:
        likelyhood = likelyhood * probability

    bayes_prob_SV_NS = (likelyhood / P_data_SupV_Nuc) * 100

    #inferencias para cada resultado******************************

    prom_V = (bayes_prob_IV_CS + bayes_prob_SV_CS + bayes_prob_IV_NS + bayes_prob_SV_NS ) / 4

    prom_S = (bayes_prob_IS_CS + bayes_prob_SS_CS + bayes_prob_IS_NS + bayes_prob_SS_NS) / 4

    if bayes_prob_IS_CS > bayes_prob_IV_CS :#intermedio cito

        prom_IC = bayes_prob_IS_CS
        
    else :

        prom_IC = bayes_prob_IV_CS

    if bayes_prob_IS_NS > bayes_prob_IV_NS : #intermedio nucl

        prom_IN = bayes_prob_IS_NS
        
    else :

        prom_IN = bayes_prob_IV_NS

    if bayes_prob_SS_CS > bayes_prob_SV_CS : #sup cito

        prom_SC = bayes_prob_SS_CS
        
    else :

        prom_SC = bayes_prob_SV_CS
        
    if bayes_prob_SS_NS > bayes_prob_SV_NS : #sup nucle

        prom_SN = bayes_prob_SS_NS
        
    else :

        prom_SN = bayes_prob_SV_NS
    
    inf1 = "El tamaño de las células indica que"
    inf2 = "el estrato intermedio se encuentra"
    inf3 = "presente con una certeza del {:.2f}%".format((prom_IC+prom_IN)/2)
    inf4 = "El tamaño de las células indica que"
    inf5 = "el estrato superficial se encuentra"
    inf6 = "presente con una certeza del {:.2f}%".format((prom_SC+prom_SN)/2)

    if prom_V > 35 : #inferencia VPH

        inf7 = "Existe un riesgo del {:.2f}%".format(prom_V)
        inf8 = "de infección con VPH"

    else:

        inf7 = "Existe evidencia del {:.2f}%".format(prom_S)
        inf8 = "de tener una muestra sana"

    label1=inst_font.render(inf1, 1, color)
    label2=inst_font.render(inf2, 1, color)
    label3=inst_font.render(inf3, 1, color)
    label4=inst_font.render(inf4, 1, color)
    label5=inst_font.render(inf5, 1, color)
    label6=inst_font.render(inf6, 1, color)
    label7=inst_font.render(inf7, 1, color)
    label8=inst_font.render(inf8, 1, color)

    screen.blit(label1, (175,315))
    screen.blit(label2, (175,330))
    screen.blit(label3, (175,345))
    screen.blit(label4, (175,385))
    screen.blit(label5, (175,400))
    screen.blit(label6, (175,415))
    screen.blit(label7, (175,455))
    screen.blit(label8, (175,470))

    pg.display.update()

    selection = main_loop ()

    if selection == 'Regresar':
        return

def Non_reproductive ():

    ExoNR_probs_BS_C = []
    ExoNR_probs_BV_C = []
    ExoNR_probs_PS_C = []
    ExoNR_probs_PV_C = []
    
    P_data_BasalS_Col = 0.561
    P_data_BasalV_Col = 0.48
    P_data_PbasalS_Col = 0.561
    P_data_PbasalV_Col = 0.48
    
    clear_screen()

    inst = "Indique el tamaño promedio"
    inst2  = "del citoplasma de las células"
    selection = ""

    label=inst_font.render(inst, 1, color2)
    label1=inst_font.render(inst2, 1, color2)
    screen.blit(label, (195,195))
    screen.blit(label1, (195,215))
    
    names = ["Basófila","Disqueratocito"]

    amount = len(names)

    call_buttons ( amount, names )

    selection = main_loop ()
        

    if selection == 'Basófila':
 
        ExoNR_probs_BS_C.append(1.00)
        ExoNR_probs_PS_C.append(1.00)
        ExoNR_probs_BV_C.append(0.00)
        ExoNR_probs_PV_C.append(0.00)
        
    elif selection == 'Disqueratocito':

        ExoNR_probs_BS_C.append(0.15)
        ExoNR_probs_PS_C.append(0.15)
        ExoNR_probs_BV_C.append(0.85)
        ExoNR_probs_PV_C.append(0.85)

    if selection == 'Regresar':
        return

    clear_screen()

    inst = "Las características de"
    inst2  = "su muestra indican que:"
    selection = ""

    label=inst_font.render(inst, 1, color2)
    label1=inst_font.render(inst2, 1, color2)
    screen.blit(label, (195,200))
    screen.blit(label1, (195,220))

    pg.display.update()

    #calculo de probabilidades con teorema de bayes
    likelyhood = 1    #Basal sana por color******************************************

    for probability in data_base["Exo NR"]["Basal Sana"]:
        ExoNR_probs_BS_C.append(probability)
        
    for probability in ExoNR_probs_BS_C:
        likelyhood = likelyhood * probability

    bayes_prob_BS_C = (likelyhood / P_data_BasalS_Col) * 100

    likelyhood = 1    #Basal VPH por color******************************************

    for probability in data_base["Exo NR"]["Basal VPH"]:
        ExoNR_probs_BV_C.append(probability)
        
    for probability in ExoNR_probs_BV_C:
        likelyhood = likelyhood * probability

    bayes_prob_BV_C = (likelyhood / P_data_BasalV_Col) * 100

    likelyhood = 1    #Parabasal sana por color******************************************

    for probability in data_base["Exo NR"]["Parab Sana"]:
        ExoNR_probs_PS_C.append(probability)
        
    for probability in ExoNR_probs_PS_C:
        likelyhood = likelyhood * probability

    bayes_prob_PS_C = (likelyhood / P_data_PbasalS_Col) * 100

    likelyhood = 1    #Parabasal VPH por color******************************************

    for probability in data_base["Exo NR"]["Parab VPH"]:
        ExoNR_probs_PV_C.append(probability)
        
    for probability in ExoNR_probs_PV_C:
        likelyhood = likelyhood * probability

    bayes_prob_PV_C = (likelyhood / P_data_PbasalV_Col) * 100

    #inferencias para cada resultado******************************

    prom_B = (bayes_prob_BS_C + bayes_prob_BV_C) / 2

    prom_PB = (bayes_prob_PS_C + bayes_prob_PV_C) / 2

    prom_S = (bayes_prob_BS_C + bayes_prob_PS_C) / 2

    prom_V = (bayes_prob_BV_C + bayes_prob_PV_C) / 2


    if prom_B < 25 :  #inferencia basal

        inf1 = "Es poco probable que las células"
        inf2 = "pertenezcan al estrato basal"

    elif prom_B >= 25  :

        inf1 = "Podria considerarse la presencia del"
        inf2  = "E.B. con una certeza del {:.2f}%".format(prom_B)

    if prom_PB < 25 :  #inferencia parabasal

        inf3 = "Es poco probable que las células"
        inf4 = "pertenezcan al estrato parabasal"

    elif prom_PB >= 25  :

        inf3 = "Podria considerarse la presencia del"
        inf4  = "E.P. con una certeza del {:.2f}%".format(prom_PB)

    if prom_V > 35 : #inferencia VPH

        inf5 = "Existe un riesgo del {:.2f}%".format(prom_V)
        inf6 = "de infección con VPH"

    if prom_S > 35 :
        
        inf5 = "Existe evidencia del {:.2f}%".format(prom_S)
        inf6 = "de tener una muestra sana"

    label1=inst_font.render(inf1, 1, color)
    label2=inst_font.render(inf2, 1, color)
    label3=inst_font.render(inf3, 1, color)
    label4=inst_font.render(inf4, 1, color)
    label5=inst_font.render(inf5, 1, color)
    label6=inst_font.render(inf6, 1, color)

    screen.blit(label1, (175,315))
    screen.blit(label2, (175,330))
    screen.blit(label3, (175,370))
    screen.blit(label4, (175,385))
    screen.blit(label5, (175,425))
    screen.blit(label6, (175,440))

    pg.display.update()

    selection = main_loop ()

    if selection == 'Regresar':
        return
        
def Endocervix ():

    Endo_probs_S_D = []
    Endo_probs_C_D = []
    Endo_probs_A_D = []

    Endo_probs_S_V = []
    Endo_probs_C_V = []

    Endo_probs_A_S = []

    P_data_Cil_Disp = 0.085
    P_data_Sec_Disp = 0.0186
    P_data_Aden_Disp = 0.379
    P_data_Cil_Vac = 0.87
    P_data_Sec_Vac = 0.0421
    P_data_Aden_Sim = 0.631

    clear_screen()
    
    inst = "Selecciona la disposición"
    inst2  = "de las células en tu muestra"
    selection = ""

    label=inst_font.render(inst, 1, color2)
    label1=inst_font.render(inst2, 1, color2)
    screen.blit(label, (195,200))
    screen.blit(label1, (195,220))
    
    names = ["Aisladas","Panal de Abeja","Empalizadas"]

    amount = len(names)

    call_buttons ( amount, names )

    selection = main_loop ()

    if selection == 'Aisladas':
        
        Endo_probs_S_D.append(0.25)
        Endo_probs_C_D.append(0.25)
        Endo_probs_A_D.append(0.13)
            
    elif selection == 'Panal de Abeja':

        Endo_probs_S_D.append(0.37)
        Endo_probs_C_D.append(0.37)
        Endo_probs_A_D.append(0.35)
        
    elif selection == 'Empalizadas':

        Endo_probs_S_D.append(0.38)
        Endo_probs_C_D.append(0.38)
        Endo_probs_A_D.append(0.10)
        
    if selection == 'Regresar':
        return

    clear_screen()

    inst = "Indique si las células"
    inst2  = "presentan vacuolas o no"
    selection = ""

    label=inst_font.render(inst, 1, color2)
    label1=inst_font.render(inst2, 1, color2)
    screen.blit(label, (195,200))
    screen.blit(label1, (195,220))
    
    names = ["Sí, presentan","No, no presentan"]

    amount = len(names)

    call_buttons ( amount, names )

    selection = main_loop ()

    if selection == 'Sí, presentan':
        
        Endo_probs_S_V.append(1.00)
        Endo_probs_C_V.append(0)
            
    elif selection == 'No, no presentan':

        Endo_probs_S_V.append(0)
        Endo_probs_C_V.append(1.00)
        
    if selection == 'Regresar':
        return

    clear_screen()

    inst = "Según tamaño y forma, indique"
    inst2  = "porcenatje de similitud entre"
    inst3 =  "los núcleos de las celulas"
    selection = ""

    label=inst_font.render(inst, 1, color2)
    label1=inst_font.render(inst2, 1, color2)
    label2=inst_font.render(inst3, 1, color2)
    screen.blit(label, (195,195))
    screen.blit(label1, (195,215))
    screen.blit(label2, (195,235))

    number_box("0")

    number = number_loop ()

    if number >= 75:
        Endo_probs_A_S.append(0.18)
        
    elif number <75 and number >= 35:
        Endo_probs_A_S.append(0.55)
        
    elif number < 35:
        Endo_probs_A_S.append(0.96)  #probabilidades calculadas

    if number == 756:
        return

    clear_screen()

    inst = "Las características de"
    inst2  = "su muestra indican que:"
    selection = ""

    label=inst_font.render(inst, 1, color2)
    label1=inst_font.render(inst2, 1, color2)
    screen.blit(label, (195,200))
    screen.blit(label1, (195,220))

    pg.display.update()

    likelyhood = 1    #ciliada Disposicion******************************************

    for probability in data_base["Endo"]["Ciliada"]:
        Endo_probs_C_D.append(probability)
        
    for probability in Endo_probs_C_D:
        likelyhood = likelyhood * probability

    bayes_prob_C_D = (likelyhood / P_data_Cil_Disp) * 100

    likelyhood = 1    #secretora Disposicion***************************************

    for probability in data_base["Endo"]["Secretora"]:
        Endo_probs_S_D.append(probability)
        
    for probability in Endo_probs_S_D:
        likelyhood = likelyhood * probability

    bayes_prob_S_D = (likelyhood / P_data_Sec_Disp) * 100

    likelyhood = 1    #adeno Disposicion*******************************************

    for probability in data_base["Endo"]["Adeno"]:
        Endo_probs_A_D.append(probability)
        
    for probability in Endo_probs_A_D:
        likelyhood = likelyhood * probability

    bayes_prob_A_D = (likelyhood / P_data_Aden_Disp) * 100

    likelyhood = 1    #ciliada vacuolas *****************************************

    for probability in data_base["Endo"]["Ciliada"]:
        Endo_probs_C_V.append(probability)
        
    for probability in Endo_probs_C_V:
        likelyhood = likelyhood * probability

    bayes_prob_C_V = (likelyhood / P_data_Cil_Vac) * 100

    likelyhood = 1    #secretora vacuolas ***************************************

    for probability in data_base["Endo"]["Secretora"]:
        Endo_probs_S_V.append(probability)
        
    for probability in Endo_probs_S_V:
        likelyhood = likelyhood * probability

    bayes_prob_S_V = (likelyhood / P_data_Sec_Vac) * 100

    likelyhood = 1    #adeno similitud*******************************************

    for probability in data_base["Endo"]["Adeno"]:
        Endo_probs_A_S.append(probability)
        
    for probability in Endo_probs_A_S:
        likelyhood = likelyhood * probability

    bayes_prob_A_S = (likelyhood / P_data_Aden_Sim) * 100

    #Inferencias para cada resultado******************************

    prom_C = (bayes_prob_C_D + bayes_prob_C_V) / 2

    prom_S = (bayes_prob_S_D + bayes_prob_S_V) / 2

    prom_A = (bayes_prob_A_D + bayes_prob_A_S) / 2

    

    if prom_C < 25 :  #inferencia ciliada

        inf1 = "Es poco probable que las"
        inf2  = "células sean ciliadas"

    elif prom_C >= 25  :

        inf1 = "Podria considerarse a las células como"
        inf2  = "ciliadas con seguridad del {:.2f}%".format(prom_C)

    if prom_S < 25 :  #inferencia secretora

        inf3 = "Es poco probable que"
        inf4  = "las células sean secretoras"

    elif prom_S >= 25 :

        inf3 = "Podria considerarse a las células como"
        inf4  = "secretoras con seguridad del {:.2f}%".format(prom_S) 

    if prom_A < 25 :  #inferencia Adeno

        inf5 = "Es poco probable que"
        inf6  = "las células sean adenocarcinomas"

    elif prom_A >= 25 :

        inf5 = "Podria considerarse a las células como"
        inf6  = "adenocar. con seguridad del {:.2f}%".format(prom_A)

    label1=inst_font.render(inf1, 1, color)
    label2=inst_font.render(inf2, 1, color)
    label3=inst_font.render(inf3, 1, color)
    label4=inst_font.render(inf4, 1, color)
    label5=inst_font.render(inf5, 1, color)
    label6=inst_font.render(inf6, 1, color)
    
    screen.blit(label1, (175,315))
    screen.blit(label2, (175,330))
    screen.blit(label3, (175,370))
    screen.blit(label4, (175,385))
    screen.blit(label5, (175,425))
    screen.blit(label6, (175,440))

    pg.display.update()

    selection = main_loop ()
    
    if selection == 'Regresar':
        return

def Transition_zone ():

    TZ_probs_I_C = []
    TZ_probs_M_C = []
    
    TZ_probs_I_S = []
    TZ_probs_M_S = []

    P_data_Mat_Crom = 0.42
    P_data_Inmat_Crom = 0.42
    P_data_Mat_Size = 0.2645
    P_data_Inmat_Size = 0.2803
    
    clear_screen()
    
    inst = "Indique cómo es la"
    inst2  = "apariencia de la cromatina"
    selection = ""

    label=inst_font.render(inst, 1, color2)
    label1=inst_font.render(inst2, 1, color2)
    screen.blit(label, (195,200))
    screen.blit(label1, (195,220))
    
    names = ["Condensada","Distribuida"]

    amount = len(names)

    call_buttons ( amount, names )

    selection = main_loop ()

    if selection == 'Condensada':

        TZ_probs_I_C.append(1.00)
        TZ_probs_M_C.append(0)
        
    elif selection == 'Distribuida':
        
        TZ_probs_I_C.append(0)
        TZ_probs_M_C.append(1.00)

    if selection == 'Regresar':
        return

    clear_screen()

    inst = "Indique el tamaño promedio"
    inst2  = "del citoplasma de las células"
    selection = ""

    label=inst_font.render(inst, 1, color2)
    label1=inst_font.render(inst2, 1, color2)
    screen.blit(label, (195,195))
    screen.blit(label1, (195,215))

    number_box("0")

    number = number_loop ()

    if number < 12:
        TZ_probs_I_S.append(0.12)

    if number >= 12 and number <=20:
        TZ_probs_I_S.append(0.74)
    
    if number > 20:
        TZ_probs_I_S.append(0.14)

    if number < 20:
        TZ_probs_M_S.append(0.15)

    if number >= 20 and number <=35:
        TZ_probs_M_S.append(0.65)
    
    if number > 35:
        TZ_probs_M_S.append(0.20)

    if number == 756:
        return

    #probabilidades calculadas

    clear_screen()

    inst = "Las características de"
    inst2  = "su muestra indican que:"
    selection = ""

    label=inst_font.render(inst, 1, color2)
    label1=inst_font.render(inst2, 1, color2)
    screen.blit(label, (195,200))
    screen.blit(label1, (195,220))

    pg.display.update()

    likelyhood = 1    #Madura por cromat******************************************

    for probability in data_base["ZT"]["Meta M"]:
        TZ_probs_M_C.append(probability)
        
    for probability in TZ_probs_M_C:
        likelyhood = likelyhood * probability

    bayes_prob_M_C = (likelyhood / P_data_Mat_Crom) * 100
    
    likelyhood = 1    #Inmadura por cromat******************************************

    for probability in data_base["ZT"]["Meta In"]:
        TZ_probs_I_C.append(probability)
        
    for probability in TZ_probs_I_C:
        likelyhood = likelyhood * probability

    bayes_prob_I_C = (likelyhood / P_data_Inmat_Crom) * 100

    likelyhood = 1    #Madura por tamaño******************************************

    for probability in data_base["ZT"]["Meta M"]:
        TZ_probs_M_S.append(probability)
        
    for probability in TZ_probs_M_S:
        likelyhood = likelyhood * probability

    bayes_prob_M_S = (likelyhood / P_data_Mat_Size) * 100
    
    likelyhood = 1    #Inmadura por tamaño******************************************

    for probability in data_base["ZT"]["Meta In"]:
        TZ_probs_I_S.append(probability)
        
    for probability in TZ_probs_I_S:
        likelyhood = likelyhood * probability

    bayes_prob_I_S = (likelyhood / P_data_Inmat_Size) * 100

    #inferencias para cada resultado******************************

    prom_M = (bayes_prob_M_C + bayes_prob_M_S) / 2

    prom_IM = (bayes_prob_I_C + bayes_prob_I_S) / 2


    if prom_M < 25 :  #inferencia madura

        inf1 = "Es poco probable que las células"
        inf2 = "presenten metaplasia madura"

    elif prom_M >= 25  :

        inf1 = "Podria considerarse a las células"
        inf2  = "con M.M. con una certeza del {:.2f}%".format(prom_M)

    if prom_IM < 25 :  #inferencia inmadura

        inf3 = "Es poco probable que las células"
        inf4 = "presenten metaplasia inmadura"

    elif prom_IM >= 25 :

        inf3 = "Podria considerarse a las células"
        inf4 = "con M.I. con una certeza del {:.2f}%".format(prom_IM)


    label1=inst_font.render(inf1, 1, color)
    label2=inst_font.render(inf2, 1, color)
    label3=inst_font.render(inf3, 1, color)
    label4=inst_font.render(inf4, 1, color)

    screen.blit(label1, (175,315))
    screen.blit(label2, (175,330))
    screen.blit(label3, (175,370))
    screen.blit(label4, (175,385))
    
    pg.display.update()

    selection = main_loop ()
    
    if selection == 'Regresar':
        return
    
setup()
Main_menu()
#number_loop()
#main_loop()


    
