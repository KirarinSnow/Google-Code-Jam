<?xml version="1.0" encoding="UTF-8" ?>
<!--
  Problem: Old Magician
  Language: XSLT
  Author: KirarinSnow
  Usage: java -jar saxon9he.jar anything.xsl thisfile.xsl <input.in >output.out
  Comments: Using XSLT 2.0 with Saxon.
 -->


<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0">
  <xsl:output method="text"/>
  <xsl:template match="*">
    <xsl:for-each select="remove(tokenize(normalize-space(
			  unparsed-text('/dev/stdin', 'utf-8')), ' '), 1)">
      <xsl:if test="position() mod 2 = 0">
	<xsl:text>Case #</xsl:text>
        <xsl:value-of select="position() div 2" />
	<xsl:text>: </xsl:text>
	<xsl:choose>
          <xsl:when test="number(.) mod 2 = 1">BLACK</xsl:when>
	  <xsl:otherwise>WHITE</xsl:otherwise>
        </xsl:choose>
        <xsl:text>&#10;</xsl:text>
      </xsl:if>
    </xsl:for-each>
  </xsl:template>
</xsl:stylesheet>
