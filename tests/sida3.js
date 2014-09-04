QUnit.test( "Assert correct property chain", function( assert ) {
    assert.equal( typeof foo, 'object', 'There should be an Object called foo' );
    assert.equal( typeof foo.name, 'string', 'foo should have a name' );
    assert.equal( typeof bar, 'object', 'There should be an Object called bar')
    assert.ok( Object.getPrototypeOf(bar) === foo, 'The prototype of bar should be foo' );
    assert.equal( bar.name, 'Kalle', "Bar should be called something else!" );
    assert.ok( bar.hasOwnProperty('name') === false, "Bar should get it's name from the [[prototype]]" );
});
