var React = require('react');

var Slide = React.createClass({
	propTypes: {
		event:   React.PropTypes.func
	},
		
	eventHandler: function(e) {
		if (typeof this.props.event === 'function') {
			this.props.event(e.target.value);
		}
	},
		
    render: function() {
		var event;
		var slide = this.props;
		var iconGroup = "";
		if (slide.icon != ""){
			iconGroup = slide.icon;
		}
	    return (
			<div className={this.props.idkey}>
			<h2 className="section-heading black-text">{slide.title}
			<div dangerouslySetInnerHTML={{__html: iconGroup}} />
			</h2>
			<h3 className="section-subheading text-muted">{this.props.content}</h3>
			<a onClick={slide.onClick} href={slide.button.href} className="plain-button" id={slide.button.idkey}>{slide.button.text}</a>
	        </div>
	    );
    }
});

module.exports = Slide;