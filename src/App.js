import React from "react";
import "./App.css";
import 'rsuite/dist/styles/rsuite-default.css';
import MySidebar from "./components/Sidebar";
import Introduction from "./components/Introduction";
import { Container, Header, Content, Footer, Sidebar, Divider} from "rsuite";
// import About from "./components/About";
// import Projects from "./components/Projects";
// import Blog from "./components/Blog";
import Timeline from "./components/Timeline";

class App extends React.Component {
  render() {
    // var sideBarStyle = { "height": "100vh" };
    return (
      <div>
        <Container>
          <Sidebar>
            <MySidebar></MySidebar>
          </Sidebar>
            <Content>
              {/* <About></About> */}
              {/* <Projects></Projects> */}
              {/* <Blog></Blog> */}
              <Introduction></Introduction>
              <Timeline></Timeline>
            </Content>
        </Container>
      </div>
    );
  }
}

export default App;
