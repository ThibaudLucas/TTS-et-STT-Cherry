#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Boucle permettant de tenir une conversation avec le robot

pico = 'sh ~/Documents/Cherry/pico.sh' #Chemin vers le script pico, qui lance pico2wave

import sys
import os
import speech_recognition as sr
import urllib2
import urllib
from test_bdd import RechercheFichiers
from voice_recognition import voice_recognition
from choix_document import ChoixDocument
from ReponseRobot import ReponseRobot

while(1):

	sauveinput = ""
	vartemp =""
	vraiesvar =""
	nom=""
	noreut=""
	var=""

	while(1):

		msg = voice_recognition()

		if (msg == "j'ai reçu un message") or (msg == "il y a quelque chose pour moi") or (msg =="y a quelque chose pour moi"):

			print("toto")
			(urls,nbr_msg) = RechercheFichiers()
			os.system(pico)
			reponse = voice_recognition()
			if(nbr_msg>0):
				ChoixDocument(reponse,urls,nbr_msg)

			break		

		(sauveinput,var,vartemp,vraiesvar,nom,noreut) = ReponseRobot(msg,sauveinput,var,vartemp,vraiesvar,nom,noreut)



		os.system(pico)