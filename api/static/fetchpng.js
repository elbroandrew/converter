async function fetch_png(){
    const resp = await fetch("/fetchpng");
    if (resp.ok){
        // const data = await resp.json();
        // document.getElementById("to_change").innerHTML = "DONE!";
        // window.location.href = "/";
        const blob = await resp.blob();
        const file = window.URL.createObjectURL(blob);
        // window.location.assign(file);
        window.open(file);
        window.location.href = "/";
        
    }else{
        console.log("ERROR: cannot download PNG image. HTTP error: " + resp.status);
    }
    
}