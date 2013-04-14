<?xml version="1.0" encoding="UTF-8" ?>
<!--
  Problem: Tic-Tac-Toe-Tomek
  Language: XSLT
  Author: KirarinSnow
  Usage: java -jar saxon9he.jar anything.xsl thisfile.xsl <input.in >output.out
  Comments: Using XSLT 2.0 with Saxon.
            I chose XSLT because its name has four letters and starts and ends
            with letters in {X, O, T}. I was considering doing the other
            input set in TECO, but I don't think I have time to. :(
 -->


<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0">
  <xsl:output method="text"/>
  <xsl:template match="*">
    
    <xsl:for-each select="tokenize(normalize-space(
			  replace(replace(replace(
			  unparsed-text('/dev/stdin', 'utf-8'),
			  '\n', '#'), '##', ' '), '[0-9]+#', '')), ' ')">
      
      <xsl:text>Case #</xsl:text>
      <xsl:value-of select="position()" />
      <xsl:text>: </xsl:text>
      <xsl:variable name="grid" select="concat('#', .)" />
      
      <!-- This is hard-coded because XSLT is giving me a headache. -->
      <xsl:variable name="g" select="concat($grid, '#',
				     substring($grid, 2, 1),
				     substring($grid, 7, 1),
				     substring($grid, 12, 1),
				     substring($grid, 17, 1), '#',
				     substring($grid, 3, 1),
				     substring($grid, 8, 1),
				     substring($grid, 13, 1),
				     substring($grid, 18, 1), '#',
				     substring($grid, 4, 1),
				     substring($grid, 9, 1),
				     substring($grid, 14, 1),
				     substring($grid, 19, 1), '#',
				     substring($grid, 5, 1),
				     substring($grid, 10, 1),
				     substring($grid, 15, 1),
				     substring($grid, 20, 1), '#',
				     substring($grid, 2, 1),
				     substring($grid, 8, 1),
				     substring($grid, 14, 1),
				     substring($grid, 20, 1), '#',
				     substring($grid, 5, 1),
				     substring($grid, 9, 1),
				     substring($grid, 13, 1),
				     substring($grid, 17, 1))" />
      
      <xsl:choose>
	<xsl:when test="contains($g, 'XXXX') or
			contains($g, 'XXXT') or contains($g, 'XXTX') or
			contains($g, 'XTXX') or contains($g, 'TXXX')">
	  <xsl:text>X won</xsl:text>
	</xsl:when>
	<xsl:when test="contains($g, 'OOOO') or
			contains($g, 'OOOT') or contains($g, 'OOTO') or
			contains($g, 'OTOO') or contains($g, 'TOOO')">
	  <xsl:text>O won</xsl:text>
	</xsl:when>
	<xsl:when test="contains($grid, '.')">
	  <xsl:text>Game has not completed</xsl:text>
	</xsl:when>
	<xsl:otherwise>
	  <xsl:text>Draw</xsl:text>
	</xsl:otherwise>
      </xsl:choose>
      <xsl:text>&#10;</xsl:text>
    </xsl:for-each>
  </xsl:template>
</xsl:stylesheet>
