import requests
import os
from datetime import date, timedelta

yesterday = date.today() - timedelta(days=1)
for_date = yesterday.strftime('%Y-%m-%d')


sftp_out_dir = '/home/bahmni_support/sftp_out_dir'
if not os.path.exists(sftp_out_dir):
    os.makedirs(sftp_out_dir)

lab_results_file = os.path.join(sftp_out_dir, 'lab_results.csv')
if os.path.exists(lab_results_file):
	os.remove(lab_results_file)

radiology_orders_file = os.path.join(sftp_out_dir, 'radiology_orders.csv')
if os.path.exists(radiology_orders_file):
	os.remove(radiology_orders_file)



token_response = requests.get('http://localhost:8050/openmrs/ws/rest/v1/session', auth=('superman', 'Admin123'))
token_response.raise_for_status()
session_id = token_response.json()['sessionId']
cookies = {'reporting_session': session_id}


lab_results_params = {'name': 'Piramal Lab Results Report', 'startDate': for_date, 'endDate': for_date, 'responseType': 'text/csv', 'paperSize': 'A3', 'appName': 'reports'}

lab_results = requests.get('http://localhost:8051/bahmnireports/report', cookies=cookies, params=lab_results_params)
lab_results.raise_for_status()
file = open(lab_results_file, "w")
file.write(lab_results.text)
file.close()


radiology_orders_params = {'name': 'Piramal Radiology Orders report', 'startDate': for_date, 'endDate': for_date, 'responseType': 'text/csv', 'paperSize': 'A3', 'appName': 'reports'}

radiology_orders = requests.get('http://localhost:8051/bahmnireports/report', cookies=cookies, params=radiology_orders_params)
radiology_orders.raise_for_status()
file = open(radiology_orders_file, "w")
file.write(radiology_orders.text)
file.close()