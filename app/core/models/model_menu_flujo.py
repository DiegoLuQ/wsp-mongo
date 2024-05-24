from pydantic import BaseModel, Field, ConfigDict
from bson import ObjectId
from typing import List

# ----- Widget List
class Propiedades_Rows(BaseModel):
    id: str
    title: str
    description: str

class Filas_Lista(BaseModel):
    rows: List[Propiedades_Rows]

class Option(BaseModel):
    title: str
    rows: List[Propiedades_Rows]

class Flujo_Lista(BaseModel):
    type_msg: str
    options: List[Option]
    header: str
    body: str
    footer: str
    button: str

# ----- Menu
class Flujo_Menu(BaseModel):
    type_msg: str
    body: str
    options: list[str]
    footer: str
    sed: str

# ----- SubMenu
class Flujo_SubMenu(BaseModel):
    type_msg: str
    body: str
    options: List[str]
    footer: str
    link: str

# ----- Main
class MenuDocumento(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()),
                    alias="_id", validate_default=True)
    numero_celular: str
    nombre_empresa: str
    active:bool
    flujo_menu: dict[str, Flujo_Menu]
    flujo_submenu: dict[str, Flujo_SubMenu]
    widget_list: dict[str, Flujo_Lista]
    model_config: ConfigDict = ConfigDict(arbitrary_types_allowed=True, json_schema_extra={
        "example":   {
            "numero_celular": "56934888609",
            "nombre_empresa": "Lianweb",
            "active":False,
            "flujo_menu": {
                "hola": {
                    "type_msg": "Flujo_Menu",
                    "body": "¡ Hola !  🌟 ¡Qué emoción tenerte aquí! Soy LianBot, tu asistente virtual personalizado para ayudarte en todo lo que necesites.¿Listo para descubrir todas las increíbles posibilidades que tenemos para ti? ¡Estoy aquí para guiarte en cada paso del camino! \nPuedes navegar por estas opciones:",
                    "options": ["informacion", "servicios"],
                    "footer": "Equipo Lw",
                    "sed": "1"

                },
                "servicios": {
                    "type_msg": "Flujo_Menu",
                    "body": "¡Explora nuestro mundo de soluciones! Desde información de productos hasta detalles de contacto, estamos aquí para ayudarte a alcanzar tus objetivos empresariales.",
                    "options": ["🍃Pagina Web", "😎 Landing Page", "🤖 Chatbot"],
                    "footer": "Información Lw | lianweb.cl",
                    "sed": "2"

                },
                "informacion": {
                    "type_msg": "Flujo_Menu",
                    "body": "!Buena elección, mira las posibilidades que ofrecemos para tu negocio! Descubre cómo nuestros productos de calidad pueden llevar tu presencia en línea al siguiente nivel.",
                    "options": ["🚩Ubicación?", "🧲Redes Sociales", "✅¿Tienen página web?"],
                    "footer": "Servicios Lw | lianweb.cl",
                    "sed": "3"

                }
            },
            "flujo_submenu": {
                "personal_cod:lp1": {
                    "type_msg": "Flujo_SubMenu",
                    "body": "¡Explora nuestro mundo de soluciones! Desde información de productos hasta detalles de contacto, estamos aquí para ayudarte a alcanzar tus objetivos empresariales.",
                    "options": ["PDF-LP1", "Contratar", "Vendedor"],
                    "footer": "LP 😎 | lianweb.cl/servicios/landingpage/lp1",
                    
                    "link": "https://www.o10media.es/blog/wp-content/uploads/2023/01/tipos-paginas-web.jpg"
                },
                "pyme_cod:lp2": {
                    "type_msg": "Flujo_SubMenu",
                    "body": "!Buena elección, mira las posibilidades que ofrecemos para tu negocio! Descubre cómo nuestros productos de calidad pueden llevar tu presencia en línea al siguiente nivel.",
                    "options": ["PDF-LP2", "Contratar", "Vendedor"],
                    "footer": "LP 😎 | lianweb.cl/servicios/landingpage/lp2",
                    
                    "link": "https://www.o10media.es/blog/wp-content/uploads/2023/01/tipos-paginas-web.jpg"
                },
                "pro_cod:lp3": {
                    "type_msg": "Flujo_SubMenu",
                    "body": "Impulsa tu negocio con nuestra Landing Page Profesional. Diseño de alta calidad, contenido persuasivo y captura de leads efectiva. ¡Convierte visitantes en clientes potenciales",
                    "options": ["PDF-LP3", "Contratar", "Vendedor"],
                    "footer": "LP 😎 | lianweb.cl/servicios/landingpage/lp3",
                    
                    "link": "https://www.o10media.es/blog/wp-content/uploads/2023/01/tipos-paginas-web.jpg"
                },
                "personal_cod:pw1": {
                    "type_msg": "Flujo_SubMenu",
                    "body": "¡Inicia tu aventura digital con nuestro Plan de Página Web Personalizado! Diseñado especialmente para emprendedores valientes como tú, que están listos para llevar su presencia en línea al siguiente nivel. Con este plan, te ofrecemos una plataforma sólida y profesional que te ayudará a destacarte en el vasto mundo digital.",
                    "options": ["PDF-PW1", "Contratar", "Vendedor"],
                    "footer": "LP 😎 | lianweb.cl/servicios/paginaweb/pw1",
                    
                    "link": "https://www.o10media.es/blog/wp-content/uploads/2023/01/tipos-paginas-web.jpg"
                },
                "Pyme cod:pw2": {
                    "type_msg": "Flujo_SubMenu",
                    "body": "Maximiza el potencial de tu Pyme con nuestro paquete de diseño web, potenciado por estrategias de marketing efectivas. ¡Destaca entre la competencia y atrae a nuevos clientes hoy mismo!",
                    "options": ["PDF-PW1", "Contratar", "Vendedor"],
                    "footer": "LP 😎 | lianweb.cl/servicios/paginaweb/pw1",
                    
                    "link": "https://www.o10media.es/blog/wp-content/uploads/2023/01/tipos-paginas-web.jpg"
                },
                "basico_cod:cb1": {
                    "type_msg": "Flujo_SubMenu",
                    "body": "¿Estás listo para llevar la atención al cliente de tu negocio al siguiente nivel? Nuestros innovadores planes de chatbot están diseñados para transformar la manera en que interactúas con tus clientes, impulsar la eficiencia operativa y potenciar el crecimiento de tu empresa.",
                    "options": ["PDF-CB1", "Contratar", "Vendedor"],
                    "footer": "LP 😎 | lianweb.cl/servicios/chatbot/cb1",
                    
                    "link": "https://www.o10media.es/blog/wp-content/uploads/2023/01/tipos-paginas-web.jpg"
                },
                "pro_cod:cb2": {
                    "type_msg": "Flujo_SubMenu",
                    "body": "¿Estás listo para llevar la atención al cliente de tu",
                    "options": ["PDF-CB2", "Contratar", "Vendedor"],
                    "footer": "LP 😎 | lianweb.cl/servicios/chatbot/cb2",
                    
                    "link": "https://www.o10media.es/blog/wp-content/uploads/2023/01/tipos-paginas-web.jpg"
                },
                "avanzado_cod:cb3": {
                    "type_msg": "Flujo_SubMenu",
                    "body": "¿Estás listo para llevar la atención al cliente de tu negocio al siguiente nivel? Nuestros innovadores planes de chatbot están diseñados para transformar la manera en que interactúas con tus clientes, impulsar la eficiencia operativa y potenciar el crecimiento de tu empresa.",
                    "options": ["PDF-CB3", "Contratar", "Vendedor"],
                    "footer": "LP 😎 | lianweb.cl/servicios/chatbot/cb3",
                    
                    "link": "https://www.o10media.es/blog/wp-content/uploads/2023/01/tipos-paginas-web.jpg"
                }
            },           
            "widget_list": {
                #SERVICIOS
                "pagina_web": {
                    "type_msg": "Flujo_Lista",
                    "options": [
                        {
                            "title": "Pagina web🍃",
                            "rows": [
                                {
                                    "id": "pw1-id",
                                    "title": "Personal cod:PW1",
                                    "description": "Iniciantes Valientes"
                                },
                                {
                                    "id": "pw2-id",
                                    "title": "Pyme cod:PW2",
                                    "description": "Pyme consolidada"
                                }
                            ]
                        }
                    ],
                    "body": "Paginas web de calidad, dale a tus cliente lo mejor",
                    "header": "Listado de Planes",
                    "footer": "Lw | Calidad y Confianza",
                    "button": "Ver ☑️"

                },
                "landing_page": {
                    "type_msg": "Flujo_Lista",
                    "options": [
                        {
                            "title": "Landing Page🏃",
                            "rows": [
                                {
                                    "id": "lp1-id",
                                    "title": "Personal cod:lp1",
                                    "description": "Para Emprendedores Iniciantes"
                                },
                                {
                                    "id": "lp2-id",
                                    "title": "Pyme cod:lp2",
                                    "description": "Para Emprendedores Intermedio"
                                },
                                {
                                    "id": "lp3-id",
                                    "title": "Pro cod:lp3",
                                    "description": "Tu tienes el poder"
                                }
                            ]
                        }],
                    "body": "Landing page de calidad, dale a tus cliente lo mejor y en un solo lugar",
                    "header": "Listado de Planes",
                    "footer": "Lw | Calidad y Confianza",
                    "button": "Ver ☑️"
                },
                "chatbot": {
                    "type_msg": "Flujo_Lista",
                    "options": [{
                        "title": "Chat Bot🤖",
                        "rows": [
                            {
                                "id": "cb1-id",
                                "title": "Basico cod:cb1",
                                "description": "row-description-content"
                            },
                            {
                                "id": "cb2-id",
                                "title": "Pro cod:cb2",
                                "description": "row-description-content"
                            },
                            {
                                "id": "cb3-id",
                                "title": "Avanzado cod:cb3",
                                "description": "row-description-content"
                            }
                        ]
                    }
                    ],
                    "body": "Potencia tu negocio con nuestros chatbots inteligentes: automatiza tareas, ofrece atención al cliente 24/7 y aumenta la satisfacción del cliente.",
                    "header": "Listado de Planes",
                    "footer": "Lw | Calidad y Confianza",
                    "button": "Ver ☑️"}
            
            }
        }
    })
