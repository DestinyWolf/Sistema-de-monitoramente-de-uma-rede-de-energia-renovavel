const express = require('express');
const server = express();

var corrente = new Map();
var amperagem = 0.3;
var Ac = 0.1;
var Dc = 0.2;
var potencia = Dc*amperagem;
var total_gerado = 0.4


corrente.set('continua', Ac);
corrente.set('alternada', Dc);
corrente.set('amperagem', amperagem);
corrente.set('potencia', potencia);
corrente.set('total_gerado', total_gerado);

server.get('/', (req, res) =>{
    return res.json({mensage: 'server working'})
})
server.get('/clima', (req, res) => {
    let url = `https://api.openweathermap.org/data/2.5/weather?lat=-12.2667&lon=-38.9667&appid=1cc137a0815ef8cc3f20971c0e9646b4`;

    fetch(url).then(response => response.json())
    .then(data => {res.send(data)})
        
})

server.get('/usuario', (req,res) => {
    return res.json({usuario: 'Marcos suarte'})
});

server.get('/dados', (req, res) => {
    return res.json({continua:Dc, alternada:Ac, amp:amperagem, potencia:potencia, totalGerado:total_gerado})
})

server.listen(3000, () => {
    console.log("Servidor esta funcionando...")
});