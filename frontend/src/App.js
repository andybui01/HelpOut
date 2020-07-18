import React from "react"
import {BrowserRouter as Router,
    Switch,
    Route,
    Link,
} from "react-router-dom";

import Volunteer from './Volunteer'
import ReachOut from './ReachOut'

export default function App(){
    return (
        <Router>
            <div>
                <nav>
                    <ul>
                        <li>
                            <Link to="/">Home</Link>
                        </li>
                        <li>
                            <Link to="/volunteer">Help someone out!</Link>
                        </li>
                        <li>
                            <Link to="/reachout">I need help!</Link>
                        </li>
                    </ul>
                </nav>
            <Switch>
                <Route path="/volunteer">
                    <Volunteer />
                </Route>
                <Route path="/reachout">
                    <ReachOut />
                </Route>
                <Route path="/">
                    <Home />
                </Route>
            </Switch>
        </div>
        </Router>
    );
}

function Home() {
    return <h2>Home</h2>;
}
