import { Sidenav } from "rsuite";
import { Nav, Dropdown } from "rsuite";
import { Icon } from "rsuite";
import React from 'react';

class MySidebar extends React.Component {
  render() {
    var mystyle = {
        width: 250,
        height: 100%
      };
    return (
      <div style={{ height: 100% ; width: 250 }}>
        <Sidenav defaultOpenKeys={["2", "3"]} activeKey="1">
          <Sidenav.Body>
            <Nav>
              <Nav.Item eventKey="1" icon={<Icon icon="dashboard" />}>
                Neeraj Kumar Singh
              </Nav.Item>
              <Dropdown eventKey="2" title="Introduction">
                <Dropdown.Item eventKey="2-1">About</Dropdown.Item>
                <Dropdown.Item eventKey="2-2">Timeline</Dropdown.Item>
              </Dropdown>
              <Dropdown eventKey="3" title="Contact">
                <Dropdown.Item eventKey="3-1">Email</Dropdown.Item>
                <Dropdown.Item eventKey="3-2">Linked-In</Dropdown.Item>
                <Dropdown.Item eventKey="3-3">GitHub</Dropdown.Item>
                <Dropdown.Item eventKey="3-4">Blogger</Dropdown.Item>
                <Dropdown.Item eventKey="3-5">Contact</Dropdown.Item>
              </Dropdown>
            </Nav>
          </Sidenav.Body>
        </Sidenav>
      </div>
    );
  }
}

export default MySidebar