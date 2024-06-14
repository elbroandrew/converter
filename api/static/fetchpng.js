async function fetch_png(){
    const resp = await fetch("/fetchpng");
    if (resp.ok){
        const blob = await resp.blob();
        const file = window.URL.createObjectURL(blob);

        let link = document.createElement("a");
        link.href = file;
        link.download = "image.png";
        link.style.display = "none";
        document.body.appendChild(link);
        link.click();
        window.URL.revokeObjectURL(file);
        document.body.removeChild(link);

        window.location.href = "/";
        
    }else{
        console.log("ERROR: cannot download PNG image. HTTP error: " + resp.status);
    }
    
}