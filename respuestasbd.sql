CREATE TABLE bot_responses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    keywords VARCHAR(255),
    response VARCHAR(255)
);
-- Ejemplo de inserción de datos
INSERT INTO bot_responses (keywords, response) VALUES
('hola,hi,saludos,buenas', 'Hola, soy botCertus. ¿En qué puedo ayudarte?'),
('como,estas,va,vas,sientes', 'Estoy bien, gracias. ¿Y tú?'),
('gracias,te lo agradezco,thanks', 'Siempre a la orden'),
('sexto ciclo,sexto,cursos de sexto', 'Arquitectura y Diseño con IA');


INSERT INTO bot_responses (keywords, response) VALUES
('sexto ciclo,sexto,cursos de sexto', 'Arquitectura y Diseño con IA'),
('clase,clases,lunes','Aqui esta el link de tu clase del lunes: https://classroom46.mynaparrot.es/playback/presentation/2.3/c3a9bc6474c802b3fe982343d465dec7bf5f7b8f-1696853788644'),
('clase,clases,martes','Aqui esta el link de tu clase del martes: https://classroom48.mynaparrot.es/playback/presentation/2.3/5fd907513d6e8c66ec416a5a0021659afd9a81b5-1696938324405'),
('clase,clases,miercoles','Aqui esta el link de tu clase del miercoles: https://classroom32.mynaparrot.es/playback/presentation/2.3/159998ea0d0269cd8b0e00d10d591f28d69ab058-1697025485880","https://classroom42.mynaparrot.es/playback/presentation/2.3/26a3515bd78f68e99a61472248a92cf3cd0026fc-1697036677120'),
('clase,clases,jueves','Aqui esta el link de tu clase del jueves: https://classroom30.mynaparrot.es/playback/presentation/2.3/69db484070765fdc5b30e3620a06f0bbf6a16b10-1697124709239'),
('clase,clases,viernes','no tienes clases los viernes T_T'),
('clase,clases,sabado','no tienes clases los sabados T_T'),
('clase,clases,domingo','no tienes clases los domingos T_T')