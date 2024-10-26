import requests
file_name = 'arroz.txt'

data = {
    '41': {
        'audience': 'This ad is focused on frontend development using Vue.js',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Vue.js',
        'similarity': '1'
    },
    '42': {
        'audience': 'This ad is focused on advanced frontend techniques with Vue.js',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Vue.js',
        'similarity': '0.95'
    },
    '43': {
        'audience': 'This ad is focused on building scalable applications with Vue.js',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Vue.js',
        'similarity': '0.9'
    },
    '44': {
        'audience': 'This ad is focused on full-stack development with Vue.js',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Vue.js',
        'similarity': '0.85'
    },
    '45': {
        'audience': 'This ad is focused on Vue.js for enterprise applications',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Vue.js',
        'similarity': '0.8'
    },
    '46': {
        'audience': 'This ad is focused on learning the basics of React.js',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'React.js',
        'similarity': '1'
    },
    '47': {
        'audience': 'This ad is focused on building modern web apps with React.js',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'React.js',
        'similarity': '0.95'
    },
    '48': {
        'audience': 'This ad is focused on React.js for single-page applications',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'React.js',
        'similarity': '0.9'
    },
    '49': {
        'audience': 'This ad is focused on full-stack development with React.js',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'React.js',
        'similarity': '0.85'
    },
    '50': {
        'audience': 'This ad is focused on React.js hooks and state management',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'React.js',
        'similarity': '0.8'
    },
    '51': {
        'audience': 'This ad is focused on Angular for building dynamic web apps',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Angular',
        'similarity': '1'
    },
    '52': {
        'audience': 'This ad is focused on mastering Angular components and services',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Angular',
        'similarity': '0.95'
    },
    '53': {
        'audience': 'This ad is focused on Angular for scalable enterprise applications',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Angular',
        'similarity': '0.9'
    },
    '54': {
        'audience': 'This ad is focused on Angular for full-stack development',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Angular',
        'similarity': '0.85'
    },
    '55': {
        'audience': 'This ad is focused on reactive programming in Angular',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Angular',
        'similarity': '0.8'
    },
    '56': {
        'audience': 'This ad is focused on frontend development with Vue.js and TypeScript',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Vue.js',
        'similarity': '0.9'
    },
    '57': {
        'audience': 'This ad is focused on creating reusable components in Vue.js',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Vue.js',
        'similarity': '0.85'
    },
    '58': {
        'audience': 'This ad is focused on state management in Vue.js with Vuex',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Vue.js',
        'similarity': '0.95'
    },
    '59': {
        'audience': 'This ad is focused on integrating APIs with Vue.js applications',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Vue.js',
        'similarity': '0.8'
    },
    '60': {
        "audience": "This ad is focused on using React.js with TypeScript for scalable apps",
        "category": "Development",
        "area": "Frontend Development",
        "sub_area": "React.js",
        'similarity': '0.9'
    },
    '61': {
        "audience": "This ad is focused on learning React.js for beginners",
        "category": "Development",
        "area": "Frontend Development",
        "sub_area": "React.js",
        "similarity": "1"
    },
    '62': {
        'audience': 'This ad is focused on advanced React.js techniques',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'React.js',
        'similarity': '0.85'
    },
    '63': {
        'audience': 'This ad is focused on building interactive UI with React.js',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'React.js',
        'similarity': '0.8'
    },
    '64': {
        'audience': 'This ad is focused on server-side rendering with React.js',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'React.js',
        'similarity': '0.75'
    },
    '65': {
        'audience': 'This ad is focused on integrating REST APIs in React.js',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'React.js',
        'similarity': '0.9'
    },
    '66': {
        'audience': 'This ad is focused on Angular for building complex applications',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Angular',
        'similarity': '0.95'
    },
    '67': {
        'audience': 'This ad is focused on Angular with TypeScript',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Angular',
        'similarity': '0.85'
    },
    '68': {
        'audience': 'This ad is focused on performance optimization in Angular apps',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Angular',
        'similarity': '0.9'
    },
    '69': {
        'audience': 'This ad is focused on unit testing in Angular applications',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Angular',
        'similarity': '0.8'
    },
    '70': {
        'audience': 'This ad is focused on debugging and troubleshooting Angular apps',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Angular',
        'similarity': '0.75'
    },
    '71': {
        'audience': 'This ad is focused on state management in React.js using Redux',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'React.js',
        'similarity': '0.9'
    },
    '72': {
        'audience': 'This ad is focused on building responsive web applications with Vue.js',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Vue.js',
        'similarity': '0.95'
    },
    '73': {
        'audience': 'This ad is focused on integrating GraphQL with React.js',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'React.js',
        'similarity': '0.85'
    },
    '74': {
        'audience': 'This ad is focused on reactive forms in Angular',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Angular',
        'similarity': '0.8'
    },
    '75': {
        'audience': 'This ad is focused on creating PWA with Vue.js',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Vue.js',
        'similarity': '0.9'
    },
    '76': {
        'audience': 'This ad is focused on Angular for real-time applications',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Angular',
        'similarity': '0.85'
    },
    '77': {
        'audience': 'This ad is focused on using Vue.js with Vue Router',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Vue.js',
        'similarity': '0.95'
    },
    '78': {
        'audience': 'This ad is focused on React.js and Next.js for server-side rendering',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'React.js',
        'similarity': '0.9'
    },
    '79': {
        'audience': 'This ad is focused on testing Vue.js applications',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'Vue.js',
        'similarity': '0.8'
    },
    '80': {
        'audience': 'This ad is focused on component lifecycle in React.js',
        'category': 'Development',
        'area': 'Frontend Development',
        'sub_area': 'React.js',
        'similarity': '0.85'
    },
    
    '81': {
        'audience': 'This ad is focused on backend development with Node.js and Express',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Node.js',
        'similarity': '1'
    },
    '82': {
        'audience': 'This ad is focused on RESTful API development with Node.js',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Node.js',
        'similarity': '1'
    },
    '83': {
        'audience': 'This ad is focused on building scalable applications with Node.js',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Node.js',
        'similarity': '1'
    },
    '84': {
        'audience': 'This ad is focused on microservices architecture with Node.js',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Node.js',
        'similarity': '1'
    },
    '85': {
        'audience': 'This ad is focused on backend development using Python and Django',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Python',
        'similarity': '1'
    },
    '86': {
        'audience': 'This ad is focused on REST APIs using Python and Flask',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Python',
        'similarity': '1'
    },
    '87': {
        'audience': 'This ad is focused on building scalable applications with Python',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Python',
        'similarity': '1'
    },
    '88': {
        'audience': 'This ad is focused on backend services with Python and FastAPI',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Python',
        'similarity': '1'
    },
    '89': {
        'audience': 'This ad is focused on backend development with PHP and Laravel',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'PHP',
        'similarity': '1'
    },
    '90': {
        'audience': 'This ad is focused on building RESTful APIs with PHP',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'PHP',
        'similarity': '1'
    },
    '91': {
        'audience': 'This ad is focused on backend development using PHP and Symfony',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'PHP',
        'similarity': '1'
    },
    '92': {
        'audience': 'This ad is focused on scalable backend systems with PHP',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'PHP',
        'similarity': '1'
    },
    '93': {
        'audience': 'This ad is focused on building backend systems using C# and .NET Core',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'C#',
        'similarity': '1'
    },
    '94': {
        'audience': 'This ad is focused on building RESTful APIs with C#',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'C#',
        'similarity': '1'
    },
    '95': {
        'audience': 'This ad is focused on backend development with C# and ASP.NET',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'C#',
        'similarity': '1'
    },
    '96': {
        'audience': 'This ad is focused on scalable backend applications with C#',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'C#',
        'similarity': '1'
    },
    '97': {
        'audience': 'This ad is focused on backend development with Ruby on Rails',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Ruby',
        'similarity': '1'
    },
    '98': {
        'audience': 'This ad is focused on RESTful APIs using Ruby and Sinatra',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Ruby',
        'similarity': '1'
    },
    '99': {
        'audience': 'This ad is focused on scalable applications with Ruby on Rails',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Ruby',
        'similarity': '1'
    },
    '100': {
        'audience': 'This ad is focused on backend services using Ruby on Rails',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Ruby',
        'similarity': '1'
    },
    '101': {
        'audience': 'This ad is focused on backend development with Go and Gin',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Go',
        'similarity': '1'
    },
    '102': {
        'audience': 'This ad is focused on building microservices with Go',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Go',
        'similarity': '1'
    },
    '103': {
        'audience': 'This ad is focused on backend services with Go and Echo',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Go',
        'similarity': '1'
    },
    '104': {
        'audience': 'This ad is focused on scalable backend systems using Go',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Go',
        'similarity': '1'
    },
    '105': {
        'audience': 'This ad is focused on backend development with Java and Spring Boot',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Java',
        'similarity': '1'
    },
    '106': {
        'audience': 'This ad is focused on building REST APIs with Java and Spring Boot',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Java',
        'similarity': '1'
    },
    '107': {
        'audience': 'This ad is focused on scalable backend applications with Java',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Java',
        'similarity': '1'
    },
    '108': {
        'audience': 'This ad is focused on backend microservices using Java and Spring Cloud',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Java',
        'similarity': '1'
    },
    '109': {
        'audience': 'This ad is focused on backend development with Kotlin and Ktor',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Kotlin',
        'similarity': '1'
    },
    '110': {
        'audience': 'This ad is focused on building RESTful APIs with Kotlin',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Kotlin',
        'similarity': '1'
    },
    '111': {
        'audience': 'This ad is focused on backend services using Kotlin and Spring Boot',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Kotlin',
        'similarity': '1'
    },
    '112': {
        'audience': 'This ad is focused on scalable backend applications with Kotlin',
        'category': 'Development',
        'area': 'Backend Development',
        'sub_area': 'Kotlin',
        'similarity': '1'
    }
}

i = 41
for key in data.values():
    response = requests.post('http://127.0.0.1:8000/api/ads/ai', json=key)
    print(i)
    i+=1
    with open(file_name, 'a') as file:
        file.write(str(key))
        file.write(str(response.json()))
        file.write('\n')


    

