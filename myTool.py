import sys
import Scraper
import LogParser
import DirMonitoring
import PortScanner
import AttackDetect

try:
	while True :

		choice = input(" \n \t \t \t What do you want to do !! \n 1 - LogParser \n 2 - DirrectoryMonitoring\n 3 - PortScanner\n 4 - AttackDetection\n 5 - Scraper\n 6 - Exit\n EnterYourChoice >>  ")
		if choice == '1':
			LogParser.main()
		# AttackDetect.main()
		elif choice=='2':
			DirMonitoring.main()
		elif choice=='3':
			PortScanner.main()
		elif choice=='4':
			AttackDetect.main()
		elif choice=='5':
			Scraper.main()	
		elif choice == '6':

			break
		else :
			print("Unknown Choice")
	print('\n<> BYe <>')
except KeyboardInterrupt:
 		print(" \n <> BYe <>")
 		sys.exit()	
