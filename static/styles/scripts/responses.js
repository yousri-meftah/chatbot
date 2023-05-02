async function getBotResponse(input) {
    //rock paper scissors
    //data={"msg":input}
    console.log(input["msg"])
    

    console.log(input)
    let res=await fetch($SCRIPT_ROOT+"/chatbot",{
        method: 'POST',
        body: JSON.stringify(input),
        mode: 'cors',
        headers: {
        'Content-Type': 'application/json'
        },
    })
    let final =await res.json()
    return final['resultat'];

    // Simple responses
    if (input == "hello") {
        return "Hello there!";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    } else {
        return "Try asking something else!";
    }
}