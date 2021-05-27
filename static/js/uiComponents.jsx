

function Navbar(props) {
  return (

    <nav className="navbar">
      <ReactRouterDOM.Link
        to="/"
        className="havbar-brand d-flex justify-content-center"
      >
        <img src="/static/img/watermelon-loading.png" height="30"/>
        <span>IM_Melon</span>
      </ReactRouterDOM.Link>
      
      <section className="d-flex justify-content-center">
        <ReactRouterDOM.NavLink
          to="/subscribe"
          activeClassName="navlink-active"
          className="nav-link nav-item"
        >
          Subscribe to SMS
        </ReactRouterDOM.NavLink>
        
      </section>
    </nav>
  );
}

//<ReactRouterDOM.NavLink
          //to="/login"
          //activeClassName="navlink-active"
          //className="nav-link nav-item"
        //>
          //Admin Log In
        //</ReactRouterDOM.NavLink>
        //<ReactRouterDOM.NavLink
          //to="/admin"
          //activeClassName="navlink-active"
          //className="nav-link nav-item"
        //>
          //Admin Page
        //</ReactRouterDOM.NavLink>