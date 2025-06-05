import { Box, Text, Link, Flex } from '@chakra-ui/react';

/**
 * Footer component for the application
 * 
 * @returns {JSX.Element} Footer component
 */
const Footer = () => {
  return (
    <Box as="footer" bg="gray.100" p={4} mt={8}>
      <Flex maxW="1200px" mx="auto" direction="column" align="center">
        <Text fontSize="sm" color="gray.600">
          &copy; {new Date().getFullYear()} TURBO_AML - Latvian Company Information Platform
        </Text>
        <Text fontSize="xs" mt={1} color="gray.500">
          Data provided by{' '}
          <Link href="https://data.gov.lv" isExternal color="brand.600">
            data.gov.lv
          </Link>
        </Text>
      </Flex>
    </Box>
  );
};

export default Footer; 