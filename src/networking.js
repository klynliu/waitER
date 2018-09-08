
var socks = {};


function setup(io){
    io.on("connection", (sock) => {
        //let msg = "Hello\n";
        //sock.emit("request-id");

        let i = 50;

        /*let id;

        sock.on("generate-id", (idtext) => {
            id = idtext;
            socks[id] = sock;
            //send more stuff back
        });

        */

        function ping(){
            sock.emit("system-message", `Patients remaining: ${i}\n`);
            if(i > 0){
                i--;
            }
        };

        //1 second interval repeat forever
        setInterval(ping, 1*1000);

        sock.on("system-message", (text) => {
            console.log(`System message: ${text}`);            
        });
    });
}

module.exports.setup = setup;