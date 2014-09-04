QUnit.test( "Assert correct property chain", function( assert ) {
    assert.equal( typeof foo, 'function', 'There should be a Function called foo' );
    assert.equal( foo.call(), 2, 'Foo.call() should return 2' );
});
