function Homepage(props) {
  function Subscribe(){
    fetch("/subscibers")
      .then((response) => response.json())
      .then((Data) => {
        alert(Data); 
      });
  return (

        <h1>IM Melon</h1>,
        <form action="/login">
        <h2>Email<input type="text"></input></h2>,
        <h2>Pasword<input type="text"></input></h2>,
        <h2>Phone number<input type="text"></input></h2>,
        <h2><button onClick={Subscribe}></button></h2>
        </form>

  );
}
  return (
        <ReactRouterDOM.Route>
          <Homepage />
        </ReactRouterDOM.Route>
 
  );

  }