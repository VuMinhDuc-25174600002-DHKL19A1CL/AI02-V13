# Deploy AI02 V13 online

This repository uses Streamlit Community Cloud to run the Python app. GitHub stores the project files; it does not execute Streamlit apps itself.

1. Open https://share.streamlit.io/ and sign in with the GitHub account that owns this repository.
2. Choose **Create app** → **Yup, I have an app**.
3. Select repository `VuMinhDuc-25174600002-DHKL19A1CL/AI02-V13`, branch `main`, and main file `app.py`.
4. Deploy. The root `requirements.txt` installs the dependencies; the root `app.py` launcher extracts and starts the packaged V13 source.

The public app runs on CPU. Uploaded pictures are sent to the Streamlit host for prediction. Do not upload private or sensitive images.
