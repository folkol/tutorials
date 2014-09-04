QUnit.test( "Assert correct types", function( assert ) {
  assert.equal( typeof foo, 'number', "Foo should be a number" );
  assert.equal( typeof bar, 'boolean', "Bar should be a boolean value" );
  assert.equal( typeof baz, 'object', "Baz should be an Object" );
  assert.equal( typeof baz.name, 'string', "Baz should have a name" );
  assert.equal( baz.name, 'kalle', "Baz should have a nice name" );
});
