import React, { Component } from 'react';
import { Navbar, FormControl, Button, Container, Nav, Form } from 'react-bootstrap';

export default class Header extends Component {
    render() {
        
        return(
            <Navbar fixed="top" collapseOnSelect expand="md" bg="dark" variant="dark">
                <Container>
                    <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                    <Navbar.Collapse id="responsive-navbar-nav" >
                        <Nav className="mr-auto">
                            <Nav.Link href="/" >Home</Nav.Link>
                            <Nav.Link href="/" >About Us</Nav.Link>
                            <Nav.Link href="/" >Our Work</Nav.Link>
                            <Nav.Link href="/" >Contact</Nav.Link>
                        </Nav>
                        <Form inline>
                        <FormControl
                            type="text"
                            placeholder="Search"
                            className="mr-sm-2"
                            />
                            <Button variant="outline-info">Search</Button>
                        </Form>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
            
        )
    }
}