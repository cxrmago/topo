#!/usr/bin/env python
#-*- coding:utf-8 -*-
#TO DO
#
#Eliminar dorks obsoletos 
#agregar colores a los mensajes de salida
#Autor : Carlos a r Mago & fr33coders Gpl v3

from  rsrchtoolv001 import whoIs 
from  rsrchtoolv001 import regDns
from  rsrchtoolv001 import geoIp
from  rsrchtoolv001 import top10shodan
from  rsrchtoolv001 import ShodanSsearch as Shsearch
from  rsrchtoolv001 import urlget
from  rsrchtoolv001 import robothi
from  rsrchtoolv001 import scrawl
from  dorkerworker import opts
from lazy_nmapscan import escaner
import dns
import os
import argparse

#gb
parser = argparse.ArgumentParser(
	prog='topo.py',
	description='| Navaja Suiza para la recoleccion de datos |',
	epilog='$$[(T)ake (O)btain (P)ackets (O)utputs]$$. . its a lazy tool... . . .'
	)
parser.add_argument('ipc', action='store',help='almacena la ip')
parser.add_argument('urlc', action='store',help='almacena la url')
parser.add_argument('--options', action='store_true', help='muestra las funciones de Topo')
parser.add_argument('--change', action='store_true', help='cambia ip & url')
parser.add_argument('--dnsinf', action='store_true', help='muestra los servidores dns, Ipv4 addresses, v6, MX')
parser.add_argument('--whois', action='store_true', help='consulta who is? ')
parser.add_argument('--geoip', action='store_true', help='Coordenadas geograficas sobre la ip (Database: GeoIP2)')
parser.add_argument('--headinf', action='store_true', help='Recibe respuestas  http / https .')
parser.add_argument('--robothi', action='store_true', help='mira el archivo robots.txt ')
parser.add_argument('--dorkerworker', action='store_true', help='Dorks rapidos&furiosos')
parser.add_argument('--sourceview', action='store_true', help='mira el codigo fuente o.o.')
parser.add_argument('--shodansearch', action='store_true', help='Busqueda con Shodan')
parser.add_argument('--shtop', action='store_true', help='consulta el 10 con Shodan.')
parser.add_argument('--ntoolbox', action='store_true', help='scripts para el analizis de redes/puertos con nMap')


if(__name__ == '__main__'):
	args = parser.parse_args()
	ipc = args.ipc
	urlc = args.urlc
	if(args.ntoolbox == True):
		escaner(ipc)
	if(args.shtop == True):
		busqueda = input('ranking top > ')
		top10shodan(busqueda)
	if(args.shodansearch == True):
		busqueda = input('busqueda shodan > ')
		Shsearch(busqueda)
	if(args.sourceview == True):
		scrawl(urlc)
	if(args.dorkerworker == True):
		opts()
	if(args.robothi == True):
		robothi(urlc)
	if(args.headinf == True):
		urlget(urlc)
	if(args.geoip == True):
		geoIp(ipc, urlc)
	if(args.whois == True):
		whoIs(urlc)
	if(args.dnsinf == True):
		try:
			regDns(urlc)
		except dns.resolver.NoAnswer:
			e = dns.resolver.NoAnswer
			print("Error:%s"% e)
	if(args.change == True):
		url = input('url > ')
		ip = input('ip > ')
