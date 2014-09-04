QUnit.test( "Assert correct content structure", function( assert ) {
    assert.equal( typeof foo, 'object', 'foo should be an Object' );
    assert.equal( typeof foo.bar, 'object', 'foo should have a nested object called bar' );
    assert.equal( typeof foo.bar.name, 'string' , 'foo.bar.baz should be a string' );
    assert.equal( foo.bar.name, 'Knut', 'foo.bar should be called Knut!' );
});
