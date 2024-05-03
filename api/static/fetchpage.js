// function fetch_data(){
//     fetch("/fetchtest").then(response => response.json()).then(function(data){
//         document.getElementById("to_change").innerHTML = data['some text'];
//     });
// }

async function fetch_data(){
    const resp = await fetch("/fetchtest");
    const data = await resp.json();
    document.getElementById("to_change").innerHTML = data['some text'];
    
}