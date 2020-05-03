from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

seuuruario = "DIGITE AQUI SEU USUARIO"
suasenha = "DIGITE AQUI A SUA SENHA"
linkdafoto = "DIGITE AQUI O LINK DA FOTO QUE SERÁ COMENTADA"
class InstagramBot:


    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path="C:\\geckodriver\\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(5)
        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(5)
        self.comente_nas_fotos('biruleibe')
        self.inserircomentario()

    @staticmethod
    def digite_como_uma_pessoa(frase,onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def comente_nas_fotos(self,hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/"+seuuruario+"/following/")

        totalseguidores = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').text       
        
        print(totalseguidores)

        btn_seguidores = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
        btn_seguidores.click()
        time.sleep(5)
        scr1 = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
        
        qtdscroll = int(totalseguidores)/12

        qtdscrollround = round(qtdscroll)

        print(qtdscrollround)
        
        for i in range(0,qtdscrollround):
            time.sleep(2)
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
                
        x = 1
        global lista
        lista = []

        pega = ''
        

        while (x <= int(totalseguidores)):
        
        #for x in range(0,int(totalseguidores)):
            names = driver.find_elements_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li['+str(x)+']/div/div[1]/div[2]/div[1]/a')                                   
            pics_hrefs = [elem.get_attribute('title')for elem in names]
            
            pega = pics_hrefs

            pics_hrefs= str(pics_hrefs).replace("[", "")
            pics_hrefs=str(pics_hrefs).replace("]","")
            pics_hrefs= str(pics_hrefs).replace("'", "")
            
            

            lista.append(pics_hrefs)

            
            
            print(pics_hrefs)

            x += 1
                
        print(len(lista))
        print('----------------------------------------------------------------------------')
        print(lista)
    def inserircomentario(self):
        driver = self.driver
        driver.get(linkdafoto)


        
        
        
        loopcomenta = 0
        outroloop = 0
        for loo in lista:
            try:
                
           
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                print(loo)
                time.sleep(random.randint(2,5))
                self.digite_como_uma_pessoa('@'+str(lista[loopcomenta]),campo_comentario)
                
                time.sleep(random.randint(53,137))
                driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/button').click()
                time.sleep(5)
                loopcomenta += 1
                outroloop += 1 

                if outroloop == 53:
                    print('PAUSA OBRIGATORIA DO INSTAGRAM-O SISTEMA CONTINUA A 1 HORA!')
                    outroloop = 0
                    time.sleep(3600)
            except Exception as e:
                print(e)
                time.sleep(5)



        
      

        


mateusBot = InstagramBot(seuuruario,suasenha)
mateusBot.login()