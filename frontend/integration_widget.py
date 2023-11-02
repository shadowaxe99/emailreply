import React from 'react';
import { connect } from 'react-redux';
import { customizeDraft, provideFeedback } from '../actions';

class IntegrationWidget extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            suggested_replies: [],
            feedback: ''
        };
    }

    componentDidMount() {
        window.addEventListener('message', this.handleMessage);
    }

    componentWillUnmount() {
        window.removeEventListener('message', this.handleMessage);
    }

    handleMessage = (event) => {
        if (event.data.type === 'suggestedRepliesGenerated') {
            this.setState({ suggested_replies: event.data.suggested_replies });
        }
    }

    handleDraftChange = (index, event) => {
        let newDrafts = [...this.state.suggested_replies];
        newDrafts[index] = event.target.value;
        this.setState({ suggested_replies: newDrafts });
    }

    handleFeedbackChange = (event) => {
        this.setState({ feedback: event.target.value });
    }

    handleSendFeedback = () => {
        this.props.provideFeedback(this.state.feedback);
        this.setState({ feedback: '' });
    }

    render() {
        return (
            <div id="replyDraftingInterface">
                {this.state.suggested_replies.map((reply, index) => (
                    <textarea key={index} value={reply} onChange={this.handleDraftChange.bind(this, index)} />
                ))}
                <button onClick={this.props.customizeDraft.bind(this, this.state.suggested_replies)}>Customize Draft</button>
                <div id="feedbackInterface">
                    <textarea value={this.state.feedback} onChange={this.handleFeedbackChange} />
                    <button onClick={this.handleSendFeedback}>Send Feedback</button>
                </div>
            </div>
        );
    }
}

const mapDispatchToProps = {
    customizeDraft,
    provideFeedback
};

export default connect(null, mapDispatchToProps)(IntegrationWidget);