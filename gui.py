import streamlit as st
from donorView import BloodDonorManager
donor_instance = BloodDonorManager()

tab1,tab2 = st.tabs(["Add Donor","View Donor"])#Buttons
blood_groups = ["A","B","c"]

with tab1:   #headings
    st.header("ADD NEW Donors..!")  # detailss
    name = st.text_input("Enter Donor Name : ")
    phone = st.text_input("Enter Donor phone : ")
    blood_group = st.selectbox("select Donor Blood Group",["A","B","o"])
    city = st.text_input("Enter Donor city : ")
    last_donation = st.date_input("Enter last donation date : ")
    if st.button("Submit"):
        donor_instance.post(name = name , blood_group = blood_group , phone = phone ,city = city , last_donation = last_donation )
        st.success("Donor Added Sucessfully....")
    
    
with tab2:
    st.header("View blood Donor details")
    records=donor_instance.get()
    print("___")
    print(records)
    if records:
        st.write(records)
    else:
        st.warning("no donors found..!")
        
  
with tab3:
    st.title("Update Donors")
    records = donor_instance.get()
    if records:
        donor_ids = [r[0]for r in records]
        id = st.selectbox("Select Donor ID", donor_ids, keys = "update_id")
          
        record = donor_instance.get_object(id=id)
        name = st.text_input("Enter your name : ",value = record[1])
        phone = st.text_input("Enter your phone : ",value = record[3])
        blood_group = st.selectbox("Enter your blood_group : ",     
                                   blood_groups,
                                   index = blood_groups.index(record[2]),
                                   key = "update_group"
                                   )
        city = st.text_input("Enter your city : ",value = record[4])
        last_donation = st.date_input("last donation date ",value = record[5])
        
        if st.button("update"):
            status,message = donor_instance.put(id = id,
                                            name = name,
                                            phone=phone,
                                            blood_group = blood_group,
                                            city = city,
                                            last_donation = last_donation)
            if status:
                st.sucess(message)
            else:
                st.error(message)
            
    else:
        st.warning("No donors found")
        
        
        
    


                               


       
    
