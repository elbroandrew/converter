async function fetch_png(){
    const resp = await fetch("/fetchpng");
    if (resp.ok){
        // const data = await resp.json();
        // document.getElementById("to_change").innerHTML = "DONE!";
        // window.location.href = "/";
        console.log(resp)
        const blob = await resp.blob();
        const file = window.URL.createObjectURL(blob);
        // window.location.assign(file);
        // window.open(file);
        // window.location.href = "/";

        let link = document.createElement("a");
        link.href = file;
        link.download = "image.png";
        link.style.display = "none";
        document.body.appendChild(link);
        link.click();
        window.URL.revokeObjectURL(file);
        document.body.removeChild(link);
        
    }else{
        console.log("ERROR: cannot download PNG image. HTTP error: " + resp.status);
    }
    
}