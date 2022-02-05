import logging
import logging.config
import csv

logging.config.fileConfig('logging.conf')
logger = logging.getLogger()

line_count = 0
data_header = []
employee = []
customer_USA_only_list = []
customer = None

logger.info('Open file{0}'.format("TEST",))
try:
    with open("customers.csv", "r") as customer_data:
        customer_reader = csv.reader(customer_data, delimiter=',', quotechar=)
