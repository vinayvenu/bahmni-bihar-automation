#!/bin/bash

python create_sftp_files.py

FILE_DATE=`date +%Y-%m-%d -d "yesterday"`

USER=$1
SFTP_SERVER=$2
HOME_DIR=/home/bahmni_support
SFTP_OUT_DIR=${HOME_DIR}/sftp_out_dir

sftp -i ${HOME_DIR}/.ssh/sftp_key_rsa ${USER}@${SFTP_SERVER} << EOF
	put ${SFTP_OUT_DIR}/lab_results.csv /${USER}/${FILE_DATE}_lab_results.csv
	put ${SFTP_OUT_DIR}/radiology_orders.csv /${USER}/${FILE_DATE}_radiology_orders.csv
EOF