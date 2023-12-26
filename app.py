import streamlit as st
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
import base64


# Function to replace text in the DOCX document
def replace_text_in_paragraph(paragraph, key, value):
    full_text = ''.join(run.text for run in paragraph.runs)
    if key in full_text:
        new_text = full_text.replace(key, value)
        for run in paragraph.runs:
            run.text = ''
        paragraph.runs[0].text = new_text


# Function to fill in the lease template with user data
def fill_lease_template(lease_data,
                        template_path='templates/lease_template.docx'):
    doc = Document(template_path)
    for paragraph in doc.paragraphs:
        for key, value in lease_data.items():
            placeholder = '{{' + key + '}}'
            replace_text_in_paragraph(paragraph, placeholder, value)
    return doc


# Function to download the filled lease document
def download_link(object_to_download, download_filename, download_link_text):
    b64 = base64.b64encode(object_to_download.read()).decode()
    href = f'<a href="data:file/docx;base64,{b64}" ' \
           f'download="{download_filename}">{download_link_text}</a>'
    return href


# Streamlit UI
st.title("Lease Agreement Form")

with st.form(key='lease_form'):
    tenant_name = st.text_input("Tenant Name(s)")
    property_address = st.text_input("Property Address")
    property_city = st.text_input("City")
    property_zipcode = st.text_input("Property Zipcode")
    date_of_agreement = st.date_input("Date of Agreement")
    from_date = st.date_input("Lease Start Date")
    rent_period = st.text_input("Lease Term")
    monthly_rent = st.text_input("Monthly Rent ($)")
    security_deposit = st.text_input("Security Deposit ($)")
    payment_details = st.text_input("Bank or Zelle Details")
    landlord_name = st.text_input("Landlord's Name")
    property_management_company = st.text_input("Property Management Company")
    property_management_address = st.text_input("Property Management Address")
    submit_button = st.form_submit_button(label='Generate Lease')

if submit_button:
    lease_data = {
        "tenant_name": tenant_name,
        "property_address": property_address,
        "property_city": property_city,
        "property_zipcode": property_zipcode,
        "date_of_agreement": str(date_of_agreement),
        "from_date": str(from_date),
        "rent_period": rent_period,
        "monthly_rent": monthly_rent,
        "security_deposit": security_deposit,
        "payment_details": payment_details,
        "landlord_name": landlord_name,
        "property_management_company": property_management_company,
        "property_management_address": property_management_address
    }

    lease_doc = fill_lease_template(lease_data)
    lease_file_docx = BytesIO()
    lease_doc.save(lease_file_docx)
    lease_file_docx.seek(0)

    # Display a preview (simplified view) of the lease agreement
    preview_text = f"""
    **Lease Agreement Preview**
    - Tenant Name: {tenant_name}
    - Property Address: {property_address}
    - City: {property_city}
    - ZIP Code: {property_zipcode}
    - Date of Agreement: {str(date_of_agreement)}
    - Lease Start Date: {str(from_date)}
    - Lease Term: {rent_period}
    - Monthly Rent: {monthly_rent}
    - Security Deposit: {security_deposit}
    - Bank or Zelle details: {payment_details}
    - Landlord's Name: {landlord_name}
    - Property Management Company: {property_management_company}
    - Property Management Address: {property_management_address}
    """
    st.markdown(preview_text)

    # Define the custom filename
    formatted_date = date_of_agreement.strftime("%Y%m%d")  # Format the date
    custom_filename = f"Lease_Agreement_{tenant_name.replace(' ', '_')}_" \
                      f"{formatted_date}.docx"

    # Display download links
    st.markdown(download_link(lease_file_docx, custom_filename,
                              'Download Lease Agreement (DOCX)'),
                unsafe_allow_html=True)

