function App() {
  const [user, setUser] = React.useState(false);

  return (
    <React.Fragment>
      <Navbar />
      <div className="container-fluid row">
        
        <ReactRouterDOM.Route exact path="/">
          <Homepage />
        </ReactRouterDOM.Route>
        
        <ReactRouterDOM.Route exact path="/subscribe">
          <Subscribe />
        </ReactRouterDOM.Route>
      
           
      <ReactRouterDOM.Route exact path="/admin">
        <Admin user={user}/>
      </ReactRouterDOM.Route>
      </div>
    </React.Fragment>
  );
}

ReactDOM.render(
  <ReactRouterDOM.BrowserRouter>
    <App />
  </ReactRouterDOM.BrowserRouter>,
  document.querySelector("#root")
);
