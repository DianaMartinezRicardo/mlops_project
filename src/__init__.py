import logging
from dotenv import load_dotenv

import dagshub

load_dotenv()


# Initialize DagsHub with credentials
dagshub.init(
	repo_owner='DianaMartinezRicardo',#<your-user-name>,
	repo_name='mlops_project'#<your-repo-name>
)



# Configure the logging strategy
logging.basicConfig(
    level=logging.INFO, # DEVUG, INFO, WARNING, ERROR CRITICAL
    format="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler()
    ]
)
