import React, {useState} from 'react';
import {Button, Col, FormGroup, Input, Label, Media, Modal, ModalBody, Row} from "reactstrap";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {updateItem} from "./basketOperations";
import "./BasketItem.scss";
import {withRouter} from "react-router";

const BasketItem = ({history, item, onTrashClick}) => {

    const [sendingRequest, setSendingRequest] = useState(false);
    const [showRemoveItem, setShowRemoveItem] = useState(false);

    const updateItemQuantity = (newQuantity) => {
        try {
            setSendingRequest(true);
            updateItem(item.id, newQuantity)

        } catch (e) {
            console.log(e)

        } finally {
            setSendingRequest(false);
        }

    };

    return (
        <div>
            <Media className={"media-container"}>
                <Media
                    left
                    className={"media-img"}
                    object
                    src={item.product.photos[0].photo_url}
                    alt="product image"
                    onClick={() => history.push({
                        pathname: `/products/product/${item.product.id}`,
                        state: {
                            product: item.product
                        }
                    })}
                >
                </Media>
                <Media body className={"media-body"}>
                    <Row>
                        <Col
                            xs={"7"}
                            className={"attraction-info-body text-highlight"}
                        >
                            <Row>
                                <Col>
                                    <Media heading className={"text-header-standard media-heading"}>
                                        {item.product.name}
                                    </Media>
                                </Col>
                            </Row>
                            <Row>
                                <Col xs={8} md={4}>
                                    <FormGroup>
                                        <Label for="itemQty" className={'text-default'}>Quantity</Label>
                                        <Input type="select" name="itemQty" label="Quantity" id="itemQty"
                                               value={item.items_quantity} disabled={sendingRequest}
                                               onChange={(e) => updateItemQuantity(parseInt(e.target.value))}
                                        >
                                            <option>1</option>
                                            <option>2</option>
                                            <option>3</option>
                                            <option>4</option>
                                            <option>5</option>
                                            <option>6</option>
                                            <option>7</option>
                                            <option>8</option>
                                            <option>9</option>
                                            <option>10</option>
                                        </Input>
                                    </FormGroup>
                                </Col>
                                <Col xs={4} md={12} className={'trash-icon-wrapper'}>
                                    <div onClick={() => setShowRemoveItem(true)} className={"text-default icon-delete"}>
                                        <FontAwesomeIcon size={"2x"} icon={['far', 'trash-alt']}/>
                                    </div>
                                </Col>
                            </Row>
                        </Col>
                        <Col xs={"5"}
                             className={'item-price text-header-standard'}
                        >
                            {`${item.product.price} €`}
                        </Col>
                    </Row>
                </Media>
            </Media>
            {showRemoveItem &&
            <Modal isOpen={showRemoveItem}
                   centered={true}
                   id={'addresses-modal'}
            >
                <ModalBody className={'delete-confirmation-container'}>
                    <div className={'modal-question text-header-standard'}>Are you sure?</div>
                    <div className={'buttons-container'}>
                        <Button
                            className={'action-button'}
                            onClick={() => onTrashClick()}
                        >
                            Yes
                        </Button>
                        <Button
                            className={'action-button'}
                            onClick={() => setShowRemoveItem(false)}
                        >
                            No
                        </Button>
                    </div>
                </ModalBody>
            </Modal>}
        </div>
    )
};

export default withRouter(BasketItem);