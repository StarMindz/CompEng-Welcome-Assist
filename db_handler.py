def query_profile_information(id_or_name):
    print(f"Querying profile information for ID or name: {id_or_name}")
    # Your database query logic here
    # This is a placeholder function for demonstration purposes
    
    # For demonstration, return dummy profile information
    if id_or_name == "Yahaya_Abdurrazak":
        profile_info = {
            'name': 'Yahaya Abdurrazak',
            'imageUrl': 'profile_pics/yahya.png',
            'about': "Yahaya Abdurrazak is an enthusiastic student at Ahmadu Bello University (ABU), Zaria, where he is pursuing a degree in Computer Engineering. With a profound interest in artificial intelligence (AI) and its myriad applications, Yahaya is committed to pushing the boundaries of AI research. His journey into the realm of AI has been marked by a relentless pursuit of knowledge and a keen eye for innovation. Beyond academics, Yahaya actively engages in discussions and initiatives aimed at harnessing AI for social good. His academic prowess, coupled with his insatiable curiosity, positions him as a promising leader in the field of AI. For collaborations or inquiries, feel free to reach out to him at yahyarimi01@gmail.com.",
            'position': 'Student, Department of Computer Engineering, Ahmadu Bello University, Zaria',
            'specialization': 'Artificial Intelligence (AI) and Computer Vision',
            'contact': 'yahyarimi01@gmail.com'
        }
    elif id_or_name == "Dahiru_Ibrahim":
        profile_info =  {
            'name': 'Dahiru Ibrahim',
            'imageUrl': 'profile_pics/dahir.jpg',
            'about': "Dahiru Ibrahim is a distinguished AI specialist hailing from Nigeria. His groundbreaking work focuses on advancing AI research, particularly in the realm of low-resource African languages. With notable contributions to Computer Vision and pioneering efforts in Neural Radiance Fields, Dahiru has emerged as a trailblazer in the field of artificial intelligence. As an AI Engineer, he continues to spearhead initiatives that bridge the gap between AI technology and real-world challenges. For collaborations or inquiries, reach out to Dahiru at dahiru@abu.edu.ng.",
            'specialization': 'Computer Vision and AGI',
            'position': 'AI Engineer',
            'contact': 'dahiru@abu.edu.ng'
        }
    elif id_or_name == "Sufyan_Ibrahim":
        profile_info =  {
            'name': 'Sufyan Ibrahim',
            'imageUrl': 'profile_pics/sufyan.jpg',
            'about': "Sufyan Ibrahim is a passionate AI and ML enthusiast with a diverse academic background. Currently serving as an ML fellow at Arewa Data Science Academy and pursuing his undergraduate studies in Computer Engineering at Ahmadu Bello University, Zaria, Sufyan epitomizes the spirit of innovation and learning. His expertise lies in Machine Learning and Data Science, where he continually seeks to push the boundaries of what's possible. As a dedicated student and fellow, Sufyan is poised to make significant contributions to the field of AI. For inquiries or collaborations, contact Sufyan at u17co1054@abu.edu.ng.",
            'specialization': 'Machine Learning and Data Science',
            'position': 'Undergraduate Student and ML Fellow',
            'contact': 'u17co1054@abu.edu.ng'
        }
    elif id_or_name == "Abdullahi_Babura":
        profile_info = {
            'name': 'Abdullahi Babura',
            'imageUrl': 'profile_pics/abdul.jpg',
            'about': "Abdullahi Ahmad Babura is a distinguished academic and aspiring AI practitioner. Currently pursuing his studies as a 500-level student in the Department of Computer Engineering at ABU Zaria, Abdullahi possesses a wealth of knowledge and skills in designing intuitive user interfaces. His academic journey has equipped him with a comprehensive understanding of Artificial Intelligence, positioning him as a forward-thinking individual in the field. With a strong work ethic and collaborative spirit, Abdullahi is poised to make meaningful contributions to the advancement of AI technology. For inquiries or collaborations, contact Abdullahi at abdull6771@gmail.com.",
            'specialization': 'Artificial Intelligence',
            'position': 'Student',
            'contact': 'abdull6771@gmail.com'
        }
    elif id_or_name == "Fatima_Idris":
        profile_info= {
            'name': 'Fatima Idris',
            'imageUrl': 'profile_pics/fati.jpg',
            'about': "Fatima Idris is a dedicated professional with a robust background in computer engineering. Currently pursuing her degree at Ahmadu Bello University, Zaria, Fatima's academic journey is characterized by a relentless pursuit of excellence. Building upon her foundation in computer engineering, Fatima pursued further studies abroad, earning a Master’s Degree in Business Administration from a prestigious institution in the United Kingdom. Her advanced education equipped her with a comprehensive skill set in strategic planning and organizational leadership. As the Assistant Class Rep, Fatima demonstrates exemplary leadership qualities and a commitment to academic excellence. For inquiries or collaborations, reach out to Fatima at fatimaidris@abu.edu.ng.",
            'specialization': 'Networking',
            'position': 'Assistant Class Representative',
            'contact': 'fatimaidris@abu.edu.ng'
        }
    
    return profile_info
