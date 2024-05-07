async function fetch_png(){
    const resp = await fetch("/fetchpng");
    if (resp.ok){
        // const data = await resp.json();
        // document.getElementById("to_change").innerHTML = "DONE!";
        // window.location.href = "/";
        console.log('done');
    }else{
        console.log("ERROR: cannot download PNG image. HTTP error: " + resp.status);
    }
    
}